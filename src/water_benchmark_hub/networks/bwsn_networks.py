"""
Module contains the BWSN networks.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, download_if_necessary

from .networks import WaterDistributionNetwork
from ..meta_data import MetaData
from ..benchmarks import register


class BWSN1(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-bwsn")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the BWSN-1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        return_scenario : `bool`, optional
            If True, the network is returned as a `epyt_flow.simulation.ScenarioConfig` instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is True.

        Returns
        -------
        :class:`~epyt_flow.simulation.scenario_config.ScenarioConfig` or `str`
            If `return_scenario` is True, BWSN-1 network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the BWSN_Network_1.inp file is returned.
        """
        f_in = os.path.join(download_dir, "BWSN_Network_1.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/BWSN_Network_1.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-BWSN1", BWSN1)


class BWSN2(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-bwsn2")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the BWSN-2 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        return_scenario : `bool`, optional
            If True, the network is returned as a `epyt_flow.simulation.ScenarioConfig` instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is True.

        Returns
        -------
        :class:`~epyt_flow.simulation.scenario_config.ScenarioConfig` or `str`
            If `return_scenario` is True, BWSN-2 network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the BWSN_Network_2.inp file is returned.
        """
        f_in = os.path.join(download_dir, "BWSN_Network_2.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/BWSN_Network_2.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-BWSN2", BWSN2)
