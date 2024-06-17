"""
Module contains the EPANET example networks.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, download_if_necessary

from .networks import WaterDistributionNetwork
from ..meta_data import MetaData
from ..benchmarks import register


class Net1(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 1.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-net1")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Net1 network.

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
            If `return_scenario` is True, Net1 network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Net1.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net1.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net1.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Net1", Net1)


class Net2(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 2.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-net2")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Net2 network.

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
            If `return_scenario` is True, Net2 network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Net2.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net2.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net2.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Net2", Net2)


class Net3(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 3.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-net3")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Net3 network.

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
            If `return_scenario` is True, Net3 network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Net3.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net3.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net3.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Net3", Net3)


class Net6(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 6.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-net6")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Net6 network.

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
            If `return_scenario` is True,  Net6 network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Net6.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net6.inp")
        url = "https://github.com/OpenWaterAnalytics/WNTR/raw/main/examples/networks/Net6.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Net6", Net6)
