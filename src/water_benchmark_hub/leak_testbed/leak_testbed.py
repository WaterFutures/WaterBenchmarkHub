"""
Module provides access to the LeakTestbed benchmark.
"""
import os
import numpy as np
import pandas as pd
from enum import Enum
from pathlib import Path
from typing import Union

from epyt_flow.utils import to_seconds, get_temp_folder, unpack_zip_archive, \
    create_path_if_not_exist, download_from_gdrive_if_necessary, download_if_necessary

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


class LeakType(Enum):
    CIRCUMFERENTIAL_CRACK = (1, "Circumferential Crack", "CC")
    GASKET_LEAK = (2, "Gasket Leak", "GL")
    LONGITUDINAL_CRACK = (3, "Longitudinal Crack", "LC")
    NO_LEAK = (4, "No-Leak", "NL")
    ORIFICE_LEAK = (5, "Orifice Leak", "OL")

    def __new__(cls, num, label, abbreviation):
        obj = object.__new__(cls)
        obj._value_ = num
        obj.label = label
        obj.abbr = abbreviation
        return obj


class Demand(Enum):
    ZERO = (1, "ND")
    SMALL = (2, "0.18 LPS")
    LARGE = (3, "0.47 LPS")
    TRANSIENT = (4, "Transient")

    def __new__(cls, num, label):
        obj = object.__new__(cls)
        obj._value_ = num
        obj.label = label
        return obj


@meta_data("LeakTestbed")
class LeakTestbed(BenchmarkResource):
    """
    LeakTestbed is a laborstory-scale dataset of sensory measurements for leak
    detection and localization by Aghashahi, M., Sela, L., Banks, K.

    The benchmark comprises 280 sensory measurements, divided into:
    - 3 sensor types: accelerometer, hydrophone and dynamic pressure sensor
    - 4 leak types: orifice leak, longitudinal and circumferential cracks,
    gasket leak and no-leak
    - 2 network topologies: looped and branched
    - 6 background conditions with variations in noise and demand

    See https://data.mendeley.com/datasets/tbrnp6vrnj/1 for details.

    This module provides a function for loading the LeakTestbed data set:
    :func:`~water_benchmark_hub.leak_testbed.leak_testbed.LeakTestbed.load_data`.
    """

    @staticmethod
    def raw_to_time_series(raw_file_path, channels=1, samplerate=8000,
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

    @staticmethod
    def load_data(network: str = None, download_dir: str = None,
                  leak_types: Union[int, LeakType, list, tuple] = (1, 2, 3, 4, 5),
                  demands: Union[int, Demand, list, tuple] = (1, 2, 3, 4),
                  background_noise: bool = False,
                  verbose: bool = True) -> dict:
        """
        Loads the LeakTestbed benchmark data set.

        Parameters
        ----------
        network : `str`
            For choosing the network: Can be branched or looped.

            The default is both.
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        leak_types : either `list`, `tuple` or single value of type `LeakType`
            or `int`
            Defines subset of leaks which is to be loaded. Leaks can be
            referenced by using enum LeakType or just the number.

            The default includes all possible leak types.
        demands : either `list`, `tuple` or single value of type `Demand`
            or `int`
            Defines subset of background demands which is to be loaded. Demands
            can be referenced by using enum Demand or just the number.

            The default includes all possible background demands.
        background_noise : `bool`
            If True, scenarios with background noise are returned.

            The default is False.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `dict`
            Dictionary containing the scenario data sets. Data of each requested scenario
            can be accessed by using the scenario ID as a key.
        """

        # Accelerometer
        # https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/30110f76-4804-4512-bca5-46b8e67dffaf/file_downloaded

        # Dynamic Pressure Sensor
        # https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/3a8b5e09-0586-4f88-8202-337a53adc98c/file_downloaded

        # Hydrophone
        # https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/db8d1475-7cb4-4c60-b9e2-7d47a7d95971/file_downloaded

        download_dir = download_dir if download_dir is not None else get_temp_folder()
        download_dir = os.path.join(download_dir, 'LeakTestbed')

        files_dic = {'Accelerometer.zip': 'https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/30110f76-4804-4512-bca5-46b8e67dffaf/file_downloaded',
                     'Dynamic Pressure Sensor.zip': 'https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/3a8b5e09-0586-4f88-8202-337a53adc98c/file_downloaded',
                     'Hydrophone.zip': 'https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/db8d1475-7cb4-4c60-b9e2-7d47a7d95971/file_downloaded'}

        for k, v in files_dic.items():
            zip_dir = os.path.join(download_dir, k)
            download_if_necessary(zip_dir, v, verbose)
            unpack_zip_archive(zip_dir, download_dir)

        if network is not None and (network == 'branched' or network == 'looped'):
            network = [network]
        else:
            network = ['branched', 'looped']

        if type(leak_types) is int:
            leak_types = [LeakType(leak_types)]
        elif type(leak_types) is LeakType:
            leak_types = [leak_types]

        if type(demands) is int:
            demands = [Demand(demands)]
        elif type(demands) is Demand:
            demands = [demands]

        if background_noise:
            background_noise_folder = os.path.join(download_dir, 'Hydrophone', 'Background Noise')
            backgound_noise_file_list = [f for f in Path(background_noise_folder).glob('Background Noise*.raw') if f.is_file()]

            for j, i in enumerate(backgound_noise_file_list):
                df_temp = LeakTestbed.raw_to_time_series(i)
                df_temp = df_temp.set_index('Sample')
                df_temp = df_temp.rename(columns={'Value': 'background_noise-' + str(i).split('.')[0].split('_')[-1]})
                if j == 0:
                    df_backgound_noise = df_temp
                else:
                    df_backgound_noise = df_backgound_noise.join(df_temp)

        results = {}
        for net in network:
            net = net.capitalize()

            for leak in leak_types:
                leak_folder = LeakType(leak).label

                for demand in demands:
                    file_str = ''
                    if net == 'Branched':
                        file_str = file_str + 'BR_'
                    elif net == 'Looped':
                        file_str = file_str + 'LO_'
                    file_str = file_str + LeakType(leak).abbr + '_'
                    file_str = file_str + Demand(demand).label

                    for k in files_dic.keys():
                        tmp_path = os.path.join(download_dir, k.split('.')[0], net, leak_folder)

                        file_list = [f for f in Path(tmp_path).glob(f'{file_str}*.csv') if f.is_file()]
                        if not background_noise:
                            file_str_raw = file_str + '_NN_'
                        else:
                            file_str_raw = file_str + '_N_'
                        file_list.extend([f for f in Path(tmp_path).glob(f'{file_str_raw}*.raw') if f.is_file()])

                        for i in file_list:
                            if str(i).split('.')[-1] == 'raw':
                                df_temp = LeakTestbed.raw_to_time_series(i)
                            else:
                                df_temp = pd.read_csv(i)

                            # get sensor name from file name
                            sensor_name = str(i).split('.')[-2].split('_')[-1]
                            sensor_type = k.split('.')[0].lower().replace(' ', '_')

                            if file_str in results:
                                # append new column to existing dataframe
                                df_temp = df_temp.set_index('Sample')
                                df_temp = df_temp.rename(columns={'Value': sensor_type + '-' + sensor_name})
                                df_temp = df_temp.loc[df_temp.index <= 30]
                                results[file_str] = pd.concat([results[file_str], df_temp], axis=1, join='outer').sort_index()
                            else:
                                df_temp = df_temp.set_index('Sample')
                                df_temp = df_temp.rename(columns={'Value': sensor_type + '-' + sensor_name})
                                df_temp = df_temp.loc[df_temp.index <= 30]
                                if background_noise:
                                    df_temp = pd.concat([df_backgound_noise, df_temp], axis=1, join='outer').sort_index()
                                results[file_str] = df_temp

        return results


register("LeakTestbed", LeakTestbed)
