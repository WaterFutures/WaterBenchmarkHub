"""
Module provides access to the LeakG3PD benchmark.
"""
import os
import math
import json
import scipy
import numpy as np
import pandas as pd
from enum import Enum
from pathlib import Path

from scipy.sparse import bsr_array
from epyt_flow.simulation import ScenarioSimulator, ScenarioConfig
from epyt_flow.simulation.events import AbruptLeakage, IncipientLeakage
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.uncertainty import ModelUncertainty, UniformUncertainty
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


class RAWSource(object):
    def __init__(self, **kwargs):
        super(RAWSource, self).__init__(**kwargs)

    def raw_to_time_series(self, raw_file_path, channels=1, samplerate=8000,
                           subtype='PCM_32', endian='LITTLE'):
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

        return df


@meta_data("LeakTestbed")
class LeakTestbed(BenchmarkResource):
    """
    LeakG3PD is an updated version of the LeakDB benchmark created by
    Pilotto Figueiredo, M. , de Souza Oliveira, L., Lucca, G., Correa Yamin, A.
    , Huckembeck dos Santos, W. and da Rosa Lopes, T.

    The dataset extends LeakDB by:
    1. Tracking of leak pressure values
    2. NET3 in addition to NET1 and HANOI
    3. Leakages are represented as new junctions which are inserted at random
    points along random pipes
    4. More variability in demand patterns
    5. New storage

    The benchmark comprises 1500 leakage scenarios, 500 scenarios per network,
    under varying conditions.

    See https://github.com/matheuspilotto/LeakG3PD/ for details.

    This module provides functions for loading the LeakG3PD data set
    :func:`~water_benchmark_hub.leakg3pd.leakg3pd.LeakG3PD.load_data`, as well as for loading the scenarios:
    :func:`~water_benchmark_hub.leakg3pd.leakg3pd.LeakG3PD.load_scenarios`.
    """

    @staticmethod
    def __leak_time_to_idx(t: int, round_up: bool = False,
                           hydraulic_time_step: int = 1800):
        if round_up is False:
            return math.floor(t / hydraulic_time_step)
        else:
            return math.ceil(t / hydraulic_time_step)

    @staticmethod
    def __create_labels(s_id: int, n_time_steps: int, nodes: list[str],
                        leaks_info: dict, hydraulic_time_step: int = 1800
                        ) -> tuple[np.ndarray, scipy.sparse.bsr_array]:
        y = np.zeros(n_time_steps)

        leak_locations_row = []
        leak_locations_col = []
        if str(s_id) in leaks_info:
            for leak in leaks_info[str(s_id)]:
                t_idx_start = LeakG3PD.__leak_time_to_idx(leak["leak_start_time"] *
                                                        hydraulic_time_step)
                t_idx_end = LeakG3PD.__leak_time_to_idx(leak["leak_end_time"] * hydraulic_time_step,
                                                      round_up=True)

                leak_node_idx = nodes.index(leak["node_id"])

                for t in range(t_idx_end - t_idx_start):
                    leak_locations_row.append(t_idx_start + t)
                    leak_locations_col.append(leak_node_idx)

                y[t_idx_start:t_idx_end] = 1

        y_leak_locations = bsr_array(
            (np.ones(len(leak_locations_row)), (leak_locations_row, leak_locations_col)),
            shape=(n_time_steps, len(nodes)))

        return y, y_leak_locations


    # TODO: leak types can be list or int / LeakType
    @staticmethod
    def load_data(network: str = None, download_dir: str = None, leak_types = (1, 2, 3, 4, 5), demands = (1, 2, 3, 4), background_noise=False,
                  return_X_y: bool = False, return_features_desc: bool = False,
                  return_leak_locations: bool = False, verbose: bool = True) -> dict:
        """
        Loads the original LeakG3PD benchmark data set.

        .. warning::

            All scenarios together are a huge data set -- approx. 6GB for Net1,
            39 GB for Net3 and 15GB for Hanoi. Downloading and loading might
            take some time! Also, a sufficient amount of hard disk memory is required.

        Parameters
        ----------
        scenarios_id : `list[int]`
            List of scenarios ID that are to be loaded -- there are a total number
            of 500 scenarios per network.
        network : `str`
            For choosing the network: Can be net1, net3 or hanoi.
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        return_X_y : `bool`, optional
            If True, the data is returned together with the labels (presence of a leakage) as
            two Numpy arrays, otherwise, the data is returned as Pandas data frames.

            The default is False.
        return_features_desc : `bool`, optional
            If True and if `return_X_y` is True, the returned dictionary contains the
            features' descriptions (i.e. names) under the key "features_desc".

            The default is False.
        return_leak_locations : `bool`
            If True and if `return_X_y` is True, the leak locations are returned as well --
            as an instance of `scipy.sparse.bsr_array <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.bsr_array.html>`_.

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

        #network_desc = network.capitalize()
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

        # TODO: was wenn liste / tuple -> check later? same with demands
        if type(leak_types) is int:
            leak_types = [LeakType(leak_types)]
        elif type(leak_types) is LeakType:
            leak_types = [leak_types]

        if type(demands) is int:
            demands = [Demand(demands)]
        elif type(demands) is Demand:
            demands = [demands]

        raw_reader = RAWSource()
        results = {}
        for net in network:
            net = net.capitalize()

            for leak in leak_types:
                # TODO convert leak of type 1 to LeakType
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
                            file_str_raw = file_str + '_NN'
                        else:
                            # TODO: include sensor data from folder background noise
                            file_str_raw = file_str + '_N'
                        file_list.extend([f for f in Path(tmp_path).glob(f'{file_str_raw}*.raw') if f.is_file()])

                        for i in file_list:
                            if str(i).split('.')[-1] == 'raw':
                                # read hydrophone raw file, out: df_temp of type dataframe
                                df_temp = raw_reader.raw_to_time_series(i)
                            else:
                                # TODO: Fehler abfangen
                                df_temp = pd.read_csv(i)

                            # get sensor name from file name
                            sensor_name = str(i).split('.')[0].split('_')[-1]
                            sensor_type = k.split('.')[0].lower().replace(' ', '_')

                            if file_str in results:
                                # append new column to existing dataframe
                                # TODO join for better index management
                                df_temp = df_temp.set_index('Sample')
                                results[file_str][sensor_type + '-' + sensor_name] = df_temp['Value']
                            else:
                                df_temp = df_temp.set_index('Sample')
                                df_temp = df_temp.rename(columns={'Value': sensor_type + '-' + sensor_name})
                                results[file_str] = df_temp

        return results
        ##################################################


        zip_mapping = {"net3": "EPANET Net 3.zip", "hanoi": "Hanoi", "net1": "Net1.zip"}
        network_mapping = {"net3": "EPANET Net 3", "hanoi": "HanoiOK", "net1": "Net1OK"}
        file_ids = {"net3": "1Obbk91MyzrYDpDV7TL7s1pIwk5r3E2tl", "hanoi": "1Fc-RQAoQ658C7tshhG9f8sx72vEnJ4LU",
                           "net1": "1GZ-YxHhsjkOyp_NGRosM7wB8R6P8rf0l"}

        url_data = f'https://drive.google.com/uc?export=download&id={file_ids[network]}'

        if network == 'net1':
            leaks_info = json.loads(NET1_LEAKAGES)
        elif network == 'net3':
            leaks_info = json.loads(NET3_LEAKAGES)
        elif network == 'hanoi':
            leaks_info = json.loads(HANOI_LEAKAGES)
        else:
            ValueError(f'{network} not known. Valid network strings are net1, net3 or hanoi')

        network_desc = network.capitalize()
        download_dir = download_dir if download_dir is not None else get_temp_folder()
        download_dir = os.path.join(download_dir, network_desc)

        zip_dir = os.path.join(download_dir, zip_mapping[network])
        download_from_gdrive_if_necessary(zip_dir, url_data, verbose)
        unpack_zip_archive(zip_dir, download_dir)

        results = {}
        for s_id in scenarios_id:
            scenario_path = os.path.join(download_dir, network_mapping[network], f'Scenario-{s_id}')

            df_demands = pd.read_csv(os.path.join(scenario_path, "Node_demands.csv"), index_col=0)
            df_demands.columns = ['Demand-' + str(col) for col in df_demands.columns]

            df_pressures = pd.read_csv(os.path.join(scenario_path, "Node_pressures.csv"), index_col=0)
            df_pressures.columns = ['Pressure-' + str(col) for col in df_pressures.columns]

            df_flows = pd.read_csv(os.path.join(scenario_path, "Link_flows.csv"), index_col=0)
            df_flows.columns = ['Flow-' + str(col) for col in df_flows.columns]

            df_labels = pd.read_csv(os.path.join(scenario_path, "Labels.csv"), index_col=0)
            df_labels.columns.values[0] = "labels"

            df_final = df_labels.join([df_flows, df_pressures, df_demands], how='inner')
            df_final = df_final.reset_index().rename(columns={"index": "timestamps"})

            if return_X_y is True:
                X = df_final.drop(['labels', 'timestamps'], axis=1, inplace=False).to_numpy()
                y = df_final[['labels']].to_numpy()

                scenario_inp_path = os.path.join(scenario_path, f'{zip_mapping[network].split('.')[0]}_Scenario-{s_id}.inp')
                sim = ScenarioSimulator(f_inp_in=scenario_inp_path)
                nodes = sim.sensor_config.nodes

                _, y_leak_locations = LeakG3PD.__create_labels(s_id, X.shape[0], nodes, leaks_info)

                if return_features_desc is True and "features_desc" not in results:
                    results["features_desc"] = df_pressures.columns.tolist() + df_flows.columns.tolist() + df_demands.columns.tolist()

                if return_leak_locations is True:
                    results[s_id] = (X, y, y_leak_locations)
                else:
                    results[s_id] = (X, y)
            else:
                results[s_id] = df_final

        return results


register("LeakTestbed", LeakTestbed)
