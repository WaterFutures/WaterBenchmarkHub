"""
Module provides access to the DiTEC benchmark.
"""
import os
import numpy as np
import pandas as pd
import re
from pathlib import Path
from epyt_flow.utils import get_temp_folder
from typing import Union
from datasets import load_dataset, get_dataset_config_names, load_from_disk
from functools import reduce

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


@meta_data("DiTEC-WDN")
class DiTECWDN(BenchmarkResource):
    """
    DiTEC-WDN dataset comprises 36000 unique scenarios simulated over 24 hours
    or 1 year by H. Truong, A. Tello, A. Lazovik and V. Degeler.

    See https://www.nature.com/articles/s41597-025-06026-0 for details.

    This module provides a function for loading the DiTEC-WDN data set:
    :func:`~water_benchmark_hub.ditec_wdn.ditec_wdn.DiTECWDN.load_data`.
    """
    def raw_to_time_series(self, raw_file_path, channels=1, samplerate=8000,
                           subtype='PCM_32', endian='LITTLE'):
        """Function to read .raw hydrophone files and create a pandas Dataframe
        containing the signal and time steps.
        """
        dtype_map = {
            'PCM_16': np.int16,
            'PCM_32': np.int32,
            'PCM_64': np.int64,
            'FLOAT': np.float32,
            'DOUBLE': np.float64
        }
        dtype = dtype_map[subtype]

        if endian == 'LITTLE':
            dtype = '<' + np.dtype(dtype).str[1:]
        else:
            dtype = '>' + np.dtype(dtype).str[1:]

        signal = np.fromfile(raw_file_path, dtype=dtype)

        if channels > 1:
            signal = signal.reshape(-1, channels)
            signal = signal[:, 0]

        n_samples = len(signal)
        time_index = np.arange(n_samples) / samplerate

        df = pd.DataFrame({
            "Sample": time_index,
            "Value": signal
        })

        df = df[:240001]

        return df

    def load_data(self, network: str,
                  scenarios_id: Union[tuple, list] = (),
                  download_dir: str = None,
                  use_raw_data: bool = False,
                  verbose: bool = True) -> dict:
        """
        Loads the DiTEC-WDN benchmark data set for the requested network.

        Parameters
        ----------
        network : `str`
            The requested network name. É.g. `ctown`, `kl`, or `19pipesystem`.
        scenarios_id : `tuple` or `list`, optional
            List of scenarios requested, can be empty to request all possible
            scenarios. A scenario IDs are always integer.

            The default is an empty set. In this case, all scenarios are
            returned.
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to
            the given path.

            The default is None.
        use_raw_data : `bool`
            If True, the scenarios are not processed further after downloading
            and the network datasets are returned directly as a dict.

            The default is False.
        verbose : `bool`, optional
            If True, further information regarding the download is provided.

            The default is True.

        Returns
        -------
        `dict`
            Dictionary containing the scenario data sets. Data of each
            requested scenario can be accessed by using the scenario ID as a
            key.
        """
        if not download_dir:
            download_dir = get_temp_folder()
        folder_wdn = Path(download_dir, "ditec_wdn")

        configurations = get_dataset_config_names("rugds/ditec-wdn")

        broken = ['epanet2_6GB_1Y_node', 'Anytown_7GB_1Y_link', 'CTOWN_1GB_24H_link', 'd-town_1GB_24H_link', 'EPANET-Net-3_23GB_1Y_link', 'OBCL-1_60GB_1_node', 'OBCL-1_60GB_1_link']
        suffixes = []
        data = {}

        for conf in configurations:
            if network.lower() == conf.lower().split('_')[0]:
                if conf in broken:
                    if verbose:
                        print(f'{conf} has failed previous tests and is therefore skipped.')
                    continue

                path = os.path.join(folder_wdn, conf)
                suffix = conf.lower().split('_')[-1]

                try:
                    if os.path.exists(path):
                        data[suffix] = load_from_disk(path)
                    else:
                        size = int(re.search(r'(\d+)GB', conf).group(1))
                        if size >= 100:
                            print(f'{conf} is very large and may stall or fail due to download size.')
                        data[suffix] = load_dataset("rugds/ditec-wdn", name=conf)
                        data[suffix].save_to_disk(path)
                except:
                    if verbose:
                        print(f'{conf} has failed and is therefore skipped.')
                    continue

                suffixes.append(suffix)

        if use_raw_data:
            return data

        df = {}
        for suffix in suffixes:
            df[suffix] = data[suffix]['train'].to_pandas()
            df[suffix] = df[suffix].rename(columns=lambda x: f'{suffix.capitalize()}_{x}' if x not in ['scenario_id','time_id'] else x)
            df[suffix] = df[suffix].dropna(subset=['scenario_id', 'time_id'])
            if len(scenarios_id) > 0:
                df[suffix] = df[suffix][df[suffix]['scenario_id'].isin(scenarios_id)]

        try:
            if len(suffixes) > 1:
                df_merged = reduce(lambda suffix_left, suffix_right: pd.merge(df[suffix_left], df[suffix_right], on=['scenario_id', 'time_id'], how='outer'), suffixes)
            else:
                df_merged = df[suffixes[0]]
        except:
            print('Failed to merge link and node datasets, returning them '
                  'separately. Access using dataset[scenario_id][nodes] or '
                  'dataset[scenario_id][links].')
            res = dict()
            for suffix in suffixes:
                for key, sub_df in df[suffix].groupby("scenario_id"):
                    if len(scenarios_id) == 0 or int(key) in scenarios_id:
                        res[int(key)][suffix] = sub_df.drop(columns=['scenario_id'])
            return res

        res = dict()
        for key, sub_df in df_merged.groupby("scenario_id"):
            if len(scenarios_id) == 0 or int(key) in scenarios_id:
                res[int(key)] = sub_df.drop(columns=['scenario_id'])

        return res


register("DiTEC-WDN", DiTECWDN)
