"""
Module provides access to the Chlorine State Estimation Benchmark.
"""

import os
import random
import numpy as np
from multiprocessing import Pool
from itertools import repeat
import tarfile

from epyt_flow.simulation import ScenarioSimulator
from epyt_flow.topology import NetworkTopology
from epyt_flow.utils import get_temp_folder, robust_download, create_path_if_not_exist

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


#***********************************************************
# Class 
#***********************************************************
@meta_data("clstateestimate")
class ChlorineStateEstimation(BenchmarkResource):
    """
    Chlorine State Estimation benchmark by Hermes, Artelt, Vrachimis, 
    Polycarpou, and Hammer (2025). 

    A comprehensive benchmark for training and evaluating chlorine
    concentration estimation methodologies in water distribution 
    networks (WDNs). The dataset comprises 18,000 scenarios across the 
    **Net1**, **Hanoi**, and **CC-DBP** networks, featuring spike, 
    wave, and random chlorine injection patterns (with and without
    randomized demands). Baseline models (physic-informed GNN and 
    physic-guided RNN) are provided in the original repository. 

    See https://doi.org/10.1007/s42979-025-04008-y for details. 
    """

    #***********************************************************
    # Constants 
    #***********************************************************

    _BASE_DATA_URL = (
        "https://filedn.com/lumBFq2P9S74PNoLPWtzxG4/"
        "A-Benchmark-for-Physics-informed-Deep-Learning-of-Chlorine-States"
        "-in-Water-Distribution-Networks/data/chlorine-data/"
    )

    _DATA_URLS = {
        "Net1": _BASE_DATA_URL + "Net1.tar.gz",
        "Hanoi": _BASE_DATA_URL + "Hanoi.tar.gz",
        "CY-DBP": _BASE_DATA_URL + "CY-DBP.tar.gz",
    }

    _VALID_NETWORKS = ["Net1", "Hanoi", "CY-DBP"]
    _VALID_PATTERNS = ["spike", "random", "wave"]



    #***********************************************************
    # Internal helpers 
    #***********************************************************
    @staticmethod
    def _download_and_extract(net_desc: str, download_dir: str, 
                              verbose:bool) -> None:
        """
        Download and extract the tar.gz archive for *net-desc* if needed.
        """
        tar_path = os.path.join(download_dir, f"{net_desc}.tar.gz")
        robust_download(tar_path, ChlorineStateEstimation._DATA_URLS[net_desc], verbose)

        extract_marker = os.path.join(download_dir, "chlorine-data", net_desc)
        if not os.path.exists(extract_marker):
            if verbose:
                print(f"Extracting {net_desc}.tar.gz "
                    "(this may take a while for large archives) ...")
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(download_dir)

    @staticmethod
    def _load_with_topology(f_in: str, f_inp_in: str,
                            path_in: str) -> tuple:
        data = np.load(os.path.join(path_in, f_in))
        flow_data = data["flow_data"]
        chlorine_data = data["node_quality"]
        injection_nodes_idx = [int(n) for n in data["injection_node_idx"]]

        with ScenarioSimulator(f_inp_in=f_inp_in) as s:
            topo = s.get_topology()

        return flow_data, chlorine_data, topo, injection_nodes_idx

    @staticmethod
    def _prepare_data(flows: np.ndarray, chlorine: np.ndarray,
                      target_node_idx: int,
                      injection_nodes_idx: list[int]) -> tuple[np.ndarray, np.ndarray]:
        """
        Build (X, y) arrays from raw flow and chlorine arrays. 
        """
        X, y = [], []

        for t in range(flows.shape[0]):
            X.append(np.concatenate((
                flows[t, :].flatten(),
                chlorine[t, injection_nodes_idx].flatten(),
            )))
            y.append(chlorine[t, target_node_idx])

        return np.array(X), np.array(y)


    #***********************************************************
    # The main method
    #***********************************************************
    def load_data(self, download_dir: str = None, net_desc: str = "Net1",
                  random_demands: bool = False, cl_injection_pattern_desc: str = "spike",
                  target_node_id: str = None,
                  train_size: int = None, val_size: int = None,
                  shuffle: bool = True, verbose: bool = True) -> dict:
        """
        Load and process chlorine state estimation scenarios.

        Parameters
        ----------
        download_dir : str, optional
            Directory for caching downloaded files. 
            
            The default is ``None``.
        net_desc : str, optional
            Network name. One of ```"Net1"``, ``"Hanoi"``, ``"CY-DBP"``. 

            The default is ``"Net1"``. 
        random_demands : bool, optional
            True if scenarios with randomized demands are requested, False otherwise. 
        cl_injection_pattern_desc : str, optional
            Chlorine injection patter. One of ``"spike"``, ``"random"``, 
            ``"wave"``.

            The default ist ``"spike"``. 
        target_node_id : str, optional 
            ID of the node for which chlorine concetration is estimated. 
            If ``None``, raw unprocessed data is returned. 

            The default is ``None``.
        train_size : int, optional 
            Number of training scenarios. Only used when 
            ``target_node_id`` is set. Otherwise, no split is applied. 

            The default is ``None``. 
        val_size : int, optional
            Number of validation scenarios. Only used together with
            ``train_size``. 

            The default is ``None``. 
        shuffle: bool, optional
            If ``True``, scenarios are shuffled before the 
            train/val/test split. 

            The default is ``True``. 
        verbose: bool, optional
            If ``True``, progress messages are printed. 

            The default is ``True``. 

        Returns
        -------
        dict 
            **Raw mode** (``target_node_id=None``):

            .. code-block:: python

                {
                    "flow_data": np.ndarray,  
                    "chlorine": np.ndarray,
                    "injection_nodes_idx": list[int], 
                    "topologies": list[NetworkTopology],
                }

            **Processed mode** (``target_node_id`` set, no split): 

            .. code-block:: python

                {"X": np.ndarray, "y": np.ndarray}

            **Processed mode with split** (``target_node_id`` and 
            ``train_size`` set): 

            .. code-block:: python

                {
                    "train": (X_train, y_train),
                    "val": (X_val, y_val),
                    "test": (X_test, y_test), 
                }

        Raises
        ------
        ValueError
            If ``net_desc`` or ``cl_injection_pattern_desc`` is invalid. 


        """
        if net_desc not in self._VALID_NETWORKS:
            raise ValueError(f"'net_desc' must be one of: {self._VALID_NETWORKS}")

        if cl_injection_pattern_desc not in self._VALID_PATTERNS:
            raise ValueError(f"'cl_injection_pattern_desc' must be one of: {self._VALID_PATTERNS}")

        download_dir = download_dir if download_dir is not None else get_temp_folder()

        create_path_if_not_exist(download_dir)

        self._download_and_extract(net_desc, download_dir, verbose)

        chlorine_data_root = os.path.join(
            download_dir, "chlorine-data", net_desc,
            f"randomized_demands={random_demands}"
            f"-{cl_injection_pattern_desc}", 
        )

        files_in = sorted([
            f for f in os.listdir(chlorine_data_root) if f.endswith(".npz")
        ])

        #---------------------------
        # Raw/unprocessed mode
        #---------------------------
        if target_node_id is None:
            inp_files = [
                os.path.join(
                    download_dir, "Network", net_desc,
                    f"Scenario-{int(f.replace('.npz', '')) + 1}.inp"
                )
                for f in files_in
            ]

            X_flows, X_cl_conc, topos, inj_idx = [], [], [], None
            ncpus = os.cpu_count()
            with Pool(processes=ncpus) as pool:
                jobs = pool.starmap(
                    self._load_with_topology,
                    zip(files_in, inp_files, repeat(chlorine_data_root)),
                    chunksize=max(1, len(files_in) // ncpus),
                )

                for X_cf, X_cl, topo, inj in jobs:
                    X_flows.append(X_cf)
                    X_cl_conc.append(X_cl)
                    topos.append(topo)
                    inj_idx = inj

            return {
                "flow_data": np.array(X_flows),
                "chlorine": np.array(X_cl_conc),
                "injection_nodes_idx": inj_idx,
                "topologies": topos,
            }

        #--------------------------
        # Processed (X,y) mode
        #--------------------------
        X_all, y_all = [], []

        for f in files_in:
            data = np.load(os.path.join(chlorine_data_root, f))
            node_ids = data["node_ids"].tolist()
            flow_data = data["flow_data"]
            chlorine = data["node_quality"]

            injection_nodes_id = data["injection_node_id"]

            try:
                iter(injection_nodes_id)
            except TypeError:
                injection_nodes_id = [injection_nodes_id]
            injection_nodes_id = list(injection_nodes_id)
            injection_nodes_idx = [node_ids.index(n_id) for n_id in injection_nodes_id]

            X_, y_ = self._prepare_data(
                flow_data, chlorine,
                node_ids.index(target_node_id),
                injection_nodes_idx,
            )

            X_all.append(X_)
            y_all.append(y_)

        X_all = np.array(X_all)
        y_all = np.array(y_all)

        if train_size is None: 
            return {"X": X_all, "y": y_all}

        indices = list(range(len(y_all)))

        if shuffle:
            random.shuffle(indices)

        return {
            "train": (X_all[indices[:train_size]],
                      y_all[indices[:train_size]]),
            "val": (X_all[indices[train_size:train_size + val_size]],
                    y_all[indices[train_size:train_size + val_size]]),
            "test": (X_all[indices[:train_size + val_size:]],
                     y_all[indices[:train_size + val_size]]),
        }

    @staticmethod
    def load_network_topology(net_desc: str,
                              download_dir: str = None) -> NetworkTopology:

        """
        Loads and returns the topology of a given network.

        Parameters
        ----------
        net_desc: str
            One of ``"Net1"``, ``"Hanoi"``, ``"CY-DBP"``.
        download_dir : str, optional
            Directory where the data is stored.

        Returns
        -------
        `epyt_flow.topology.NetworkTopology`
            Topology of network.

        Raises
        ------
        ValueError
            If ``net_desc`` is invalid.

        """
        if net_desc not in ChlorineStateEstimation._VALID_NETWORKS:
            raise ValueError(f"'net_desc' must be one of: {ChlorineStateEstimation._VALID_NETWORKS}")

        download_dir = download_dir if download_dir is not None else get_temp_folder()

        return NetworkTopology.load_from_file(
            os.path.join(download_dir, "Networks", net_desc,
                         "topology.epytflow_topology")
        )

register("ClStateEstimate", ChlorineStateEstimation)
