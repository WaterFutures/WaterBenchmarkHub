"""
Module provides functions for loading different water distribution networks.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, download_if_necessary

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import MetaData


class WaterDistributionNetwork(BenchmarkResource):
    """
    Base class of water distribution networks.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise NotImplementedError()


class Richmond(WaterDistributionNetwork):
    """
    Class for loading the Richmond network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-richmond")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Richmond network.

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
            If `return_scenario` is True, Richmond network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Richmond_standard.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Richmond_standard.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "exeter-benchmarks/Richmond_standard.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Richmond", Richmond)


class Micropolois(WaterDistributionNetwork):
    """
    Class for loading the Micropolois network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-micropolois")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the MICROPOLIS network.

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
            If `return_scenario` is True, MICROPOLIS network loaded into a scenario configuration
            that can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the MICROPOLIS_v1.inp file is returned.
        """
        f_in = os.path.join(download_dir, "MICROPOLIS_v1.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/asce-tf-wdst/" + \
            "MICROPOLIS_v1.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Micropolois", Micropolois)


class Balerma(WaterDistributionNetwork):
    """
    Class for loading the Balerma network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-balerma")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Balerma network.

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
            If `return_scenario` is True, Balerma network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Balerma.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Balerma.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/Balerma.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Balerma", Balerma)


class Rural(WaterDistributionNetwork):
    """
    Class for loading the Rural network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-rural")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Rural network.

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
            If `return_scenario` is True, Rural network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the RuralNetwork.inp file is returned.
        """
        f_in = os.path.join(download_dir, "RuralNetwork.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/RuralNetwork.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Rural", Rural)


class Anytown(WaterDistributionNetwork):
    """
    Class for loading the Anytown network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-anytown")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Anytown network.

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
            If `return_scenario` is True, Anytown network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Anytown.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Anytown.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Anytown.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Anytown", Anytown)


class DTown(WaterDistributionNetwork):
    """
    Class for loading the D-Town network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-dtown")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the D-Town network.

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
            If `return_scenario` is True, D-Town network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the d-town.inp file is returned.
        """
        f_in = os.path.join(download_dir, "d-town.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/d-town.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-DTown", DTown)


class CTown(WaterDistributionNetwork):
    """
    Class for loading the C-Town network.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-ctown")

    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             return_scenario: bool = True) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the C-Town network.

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
            If `return_scenario` is True, C-Town network loaded into a scenario configuration that can
            be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the CTOWN.inp file is returned.
        """
        f_in = os.path.join(download_dir, "CTOWN.INP")
        url = "https://github.com/scy-phy/www.batadal.net/raw/master/data/CTOWN.INP"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-CTown", CTown)


class Kentucky(WaterDistributionNetwork):
    """
    Class for loading the Kentucky networks.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-kentucky")

    @staticmethod
    def load(network_id: int = 1, download_dir: str = get_temp_folder(),
             verbose: bool = True, return_scenario: bool = True
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the specified Kentucky network.

        Parameters
        ----------
        network_id : `int`, optional
            The ID (1-15) of the particular network.

            The default is wdn_id=1
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
            If `return_scenario` is True, Kentucky network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the .inp file is returned.
        """
        if not isinstance(network_id, int):
            raise ValueError("'wdn_id' must be an integer in [1, 15]")
        if network_id < 1 or network_id > 15:
            raise ValueError(f"Unknown network 'ky{network_id}.inp'")

        f_in = os.path.join(download_dir, f"ky{network_id}.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            f"asce-tf-wdst/ky{network_id}.inp"

        download_if_necessary(f_in, url, verbose)
        return load_inp(f_in)


register("Network-Kentucky", Kentucky)


class Hanoi(WaterDistributionNetwork):
    """
    Class for loading the Hanoi networks.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise MetaData.get_meta_info("network-hanoi")

    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             include_default_sensor_placement: bool = False,
             verbose: bool = True, return_scenario: bool = True
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Hanoi network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        include_default_sensor_placement : `bool`, optional
            If True, a default sensor placement will be included in the returned scenario configuration.

            The default is False
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
            If `return_scenario` is True, Hanoi network loaded into a scenario configuration that
            can be passed on to :class:`~epyt_flow.simulation.scenario_simulator.ScenarioSimulator`.
            Otherwise, the path to the Hanoi.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Hanoi.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Hanoi.inp"

        download_if_necessary(f_in, url, verbose)
        config = load_inp(f_in)

        if include_default_sensor_placement is True:
            sensor_config = config.sensor_config
            sensor_config.pressure_sensors = ["13", "16", "22", "30"]
            sensor_config.flow_sensors = ["1"]

            config = ScenarioConfig(scenario_config=config, sensor_config=sensor_config)

        return config


register("Network-Hanoi", Hanoi)
