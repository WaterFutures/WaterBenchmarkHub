"""
Module provides access to the LeakG3PD benchmark.
"""
import os
import math
import json
import scipy
import numpy as np
import pandas as pd

from scipy.sparse import bsr_array
from epyt_flow.simulation import ScenarioSimulator, ScenarioConfig
from epyt_flow.simulation.events import AbruptLeakage, IncipientLeakage
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.uncertainty import ModelUncertainty, UniformUncertainty
from epyt_flow.utils import to_seconds, get_temp_folder, unpack_zip_archive, \
    create_path_if_not_exist, download_from_gdrive_if_necessary, download_if_necessary

from .leakg3pd_data import NET1_LEAKAGES, NET3_LEAKAGES, HANOI_LEAKAGES
from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


@meta_data("LeakG3PD")
class LeakG3PD(BenchmarkResource):
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

    @staticmethod
    def load_data(scenarios_id: list[int], network: str, download_dir: str = None,
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
        # Whole drive
        # https://drive.google.com/drive/folders/1HM2xI9VpC4us7rFX4IuXXCoHDrnWfC17

        # Net1
        # https://drive.google.com/file/d/1GZ-YxHhsjkOyp_NGRosM7wB8R6P8rf0l/view?usp=drive_link

        # Hanoi
        # https://drive.google.com/file/d/1Fc-RQAoQ658C7tshhG9f8sx72vEnJ4LU/view?usp=drive_link

        # Net 3
        # https://drive.google.com/file/d/1Obbk91MyzrYDpDV7TL7s1pIwk5r3E2tl/view?usp=drive_link

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

                scenario_inp_path = os.path.join(scenario_path, f"{zip_mapping[network].split('.')[0]}_Scenario-{s_id}.inp")
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

    @staticmethod
    def load_scenarios(scenarios_id: list[int], network: str,
                       download_dir: str = None, verbose: bool = True) -> list[ScenarioConfig]:
        """
        Creates and returns LeakG3PD scenarios -- they can be either modified or
        passed directly to the EPyT-Flow simulator
        `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.

        .. note::
            Note that due to the randomness in the demand creation as well as in the model
            uncertainties, the simulation results will differ between different runs, and
            will also differ from the original data set
            (see :func:`~water_benchmark_hub.leakg3pd.leakg3pd.LeakG3PD.load_data`).
            However, the leakages (i.e. location and profile) will be always the same and be
            consistent with the original data set.

        Parameters
        ----------
        scenarios_id : `list[int]`
            List of scenarios ID that are to be loaded -- there is a total number
            of 500 scenarios per network.
        network : `str`
            For choosing the network: Can be net1, net3 or hanoi.
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `list[epyt_flow.simulation.scenario_config.ScenarioConfig] <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_
            LeakG3PD scenarios.
        """
        # It's not possible to regenerate the scenarios, since the random seed
        # for leak locations is unknown, so they have to be downloaded

        zip_mapping = {"net3": "EPANET Net 3.zip", "hanoi": "Hanoi", "net1": "Net1.zip"}
        network_mapping = {"net3": "EPANET Net 3", "hanoi": "HanoiOK", "net1": "Net1OK"}
        file_ids = {"net3": "1Obbk91MyzrYDpDV7TL7s1pIwk5r3E2tl", "hanoi": "1Fc-RQAoQ658C7tshhG9f8sx72vEnJ4LU",
                           "net1": "1GZ-YxHhsjkOyp_NGRosM7wB8R6P8rf0l"}

        url_data = f'https://drive.google.com/uc?export=download&id={file_ids[network]}'

        network_desc = network.capitalize()
        download_dir = download_dir if download_dir is not None else get_temp_folder()
        download_dir_net = os.path.join(download_dir, network_desc)

        zip_dir = os.path.join(download_dir_net, zip_mapping[network])
        download_from_gdrive_if_necessary(zip_dir, url_data, verbose)
        unpack_zip_archive(zip_dir, download_dir_net)

        scenarios_inp = []
        scenarios_configs = []

        # Set simulation duration
        hydraulic_time_step = to_seconds(minutes=30)    # 30min time steps
        general_params = {"simulation_duration": to_seconds(
            days=365),  # One year
            "hydraulic_time_step": hydraulic_time_step,
            "reporting_time_step": hydraulic_time_step}

        # Add demand patterns
        def gen_dem(download_dir, network, use_gen_dem2=False):
            # Taken from https://github.com/matheuspilotto/LeakG3PD/blob/main/LeakG3PD_Dataset_Generator_Py3/leakG3PDDatasetGenerator.py
            week_pat = scipy.io.loadmat(
                os.path.join(download_dir, "leakg3pd_weekPat_30min.mat"))
            a_w = week_pat['Aw']
            nw = week_pat['nw']
            year_offset = scipy.io.loadmat(
                os.path.join(download_dir, "leakg3pd_yearOffset_30min.mat"))
            a_y = year_offset['Ay']
            ny = year_offset['ny']

            # Create yearly component
            days = 365

            t = (288 / 6) * days  # one year period in five minute intervals
            w = 2 * np.pi / t
            k = np.arange(1, days * 288 / 6 + 1,
                          1)  # number of time steps in time series
            n = ny[0][0]  # number of fourier coefficients
            h_y = [1] * len(k)

            for i in range(1, n + 1):
                h_y = np.column_stack(
                    (h_y, np.sin(i * w * k), np.cos(i * w * k)))

            unc_y = 0.1
            a_y_r = a_y * (1 - unc_y + 2 * unc_y * np.random.rand(
                int(a_y.shape[0]), int(a_y.shape[1])))
            year_offset = np.dot(h_y, a_y_r)

            # Create weekly component
            t = (288 / 6) * 7  # one week period in five minute intervals
            w = 2 * np.pi / t
            k = np.arange(1, days * 288 / 6 + 1,
                          1)  # number of time steps in time series
            n = nw[0][0]  # number of fourier coefficients
            h_w = [1] * len(k)
            for i in range(1, n + 1):
                h_w = np.column_stack(
                    (h_w, np.sin(i * w * k), np.cos(i * w * k)))

            unc_w = 0.1
            a_w_r = a_w * (1 - unc_w + 2 * unc_w * np.random.rand(
                int(a_w.shape[0]), int(a_w.shape[1])))
            week_year_pat = np.dot(h_w, a_w_r)

            # Create random component
            unc_r = 0.05
            random = np.random.normal(0, (-unc_r + 2 * unc_r),
                                      (int(week_year_pat.shape[0]),
                                       int(week_year_pat.shape[1])))

            # Create demand
            if network == 'net1' or 'net3':
                base = 1
            elif network == 'hanoi':
                base = 0.3 # Avoid negative pressure in Hanoi

            variation = 0.75 + np.random.normal(0, 0.07)  # from 0 to 1
            dem = base * (year_offset + 1) * (
                        week_year_pat * variation + 1) * (random + 1)

            if use_gen_dem2:
                dem = np.roll(dem, int(round(
                    np.random.uniform(-4, 4))))  # +-2h time shift
                shift = np.random.rand(len(dem)).round().reshape(len(dem), 1)
                dem = shift * dem

            dem = dem.tolist()
            dem_final = []
            for d in dem:
                dem_final.append(d[0])

            return dem_final

        week_pattern_url = "https://github.com/matheuspilotto/LeakG3PD/raw/refs/heads/main/LeakG3PD_Dataset_Generator_Py3/weekPat_30min.mat"
        year_offset_url = "https://github.com/matheuspilotto/LeakG3PD/raw/refs/heads/main/LeakG3PD_Dataset_Generator_Py3/yearOffset_30min.mat"

        download_if_necessary(os.path.join(download_dir, "leakg3pd_weekPat_30min.mat"),
                              week_pattern_url, verbose)
        download_if_necessary(os.path.join(download_dir, "leakg3pd_yearOffset_30min.mat"),
                              year_offset_url, verbose)

        for s_id in scenarios_id:   # Create new .inp files with demands if necessary

            scenario_path = os.path.join(download_dir_net, network_mapping[network], f'Scenario-{s_id}')
            scenario_inp_path = os.path.join(scenario_path, f"{zip_mapping[network].split('.')[0]}_Scenario-{s_id}.inp")

            f_inp_in = os.path.join(download_dir,
                                    f"{network.capitalize()}_LeakG3PD_ID=" +
                                    f"{s_id}.inp")
            scenarios_inp.append(f_inp_in)

            if not os.path.exists(f_inp_in):
                with ScenarioSimulator(f_inp_in=scenario_inp_path) as wdn:
                    wdn.epanet_api.setTimeHydraulicStep(general_params["hydraulic_time_step"])
                    wdn.epanet_api.setTimeSimulationDuration(general_params["simulation_duration"])
                    wdn.epanet_api.setTimePatternStep(general_params["hydraulic_time_step"])
                    wdn.epanet_api.setFlowUnitsCMH()

                    wdn.epanet_api.deletePatternsAll()

                    reservoir_nodes_id = wdn.epanet_api.getNodeReservoirNameID()
                    for node_id in wdn.sensor_config.nodes:
                        if node_id in wdn.sensor_config.tanks or\
                                node_id in reservoir_nodes_id or \
                                (str(node_id).startswith('leak')):
                            continue

                        node_idx = wdn.epanet_api.getNodeIndex(node_id)
                        base_demand = wdn.epanet_api.getNodeBaseDemands(node_idx)[1][0]

                        my_demand_pattern = np.array(gen_dem(download_dir, network))

                        wdn.set_node_demand_pattern(node_id=node_id, base_demand=base_demand,
                                                    demand_pattern_id=f"demand_{node_id}",
                                                    demand_pattern=my_demand_pattern)

                    sensor_config = wdn.sensor_config
                    wdn.epanet_api.saveInputFile(f_inp_in)
            else:
                with ScenarioSimulator(f_inp_in=scenario_inp_path) as wdn:
                    sensor_config = wdn.sensor_config

            # Place pressure and flow sensors everywhere)
            sensor_config.pressure_sensors = sensor_config.nodes
            sensor_config.flow_sensors = sensor_config.links

            scenarios_configs.append(sensor_config)

        # Create uncertainties
        class MyUniformUncertainty(UniformUncertainty):
            """
            Custom uniform uncertainty for LeakG3PD scenarios.
            """
            def apply(self, data: float) -> float:
                z = data * np.random.uniform(low=self.low, high=self.high)
                lower = data - z
                upper = data + z
                return lower + np.random.uniform() * (upper - lower)

        my_uncertainty = MyUniformUncertainty(low=0, high=0.25)
        model_uncertainty = ModelUncertainty(global_pipe_length_uncertainty=my_uncertainty,
                                             global_pipe_diameter_uncertainty=my_uncertainty,
                                             global_pipe_roughness_uncertainty=my_uncertainty,
                                             global_base_demand_uncertainty=my_uncertainty)

        # Add leakages
        leaks_all = []

        if network == 'net1':
            leaks_info = json.loads(NET1_LEAKAGES)
        elif network == 'net3':
            leaks_info = json.loads(NET3_LEAKAGES)
        elif network == 'hanoi':
            leaks_info = json.loads(HANOI_LEAKAGES)
        else:
            ValueError(f'{network} not known. Valid network strings are net1, net3 or hanoi')

        for s_id in scenarios_id:
            leaks_data = []

            if str(s_id) in leaks_info:
                for leak in leaks_info[str(s_id)]:
                    leaks_data.append(
                        AbruptLeakage(node_id=leak["node_id"], link_id=None,
                                      diameter=leak["leak_diameter"],
                                      start_time=leak["leak_start_time"] * hydraulic_time_step,
                                      end_time=leak["leak_end_time"] * hydraulic_time_step))

            leaks_all.append(leaks_data)

        # Build final scenarios
        return [ScenarioConfig(f_inp_in=f_inp_in, general_params=general_params,
                               sensor_config=sensor_config, model_uncertainty=model_uncertainty,
                               system_events=leaks)
                for f_inp_in, sensor_config, leaks in zip(scenarios_inp, scenarios_configs, leaks_all)]


register("LeakG3PD", LeakG3PD)
