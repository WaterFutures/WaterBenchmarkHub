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
from ..meta_data import meta_data


class WaterDistributionNetwork(BenchmarkResource):
    """
    Base class of water distribution networks.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise NotImplementedError()


@meta_data("network-cy-dbp")
class CYDBP(WaterDistributionNetwork):
    """
    Class for loading the Richmond network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the CY-DBP network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Richmond network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the CY-DBP.inp file is returned.
        """
        f_in = os.path.join(download_dir, "CY-DBP.inp")
        url = "https://raw.githubusercontent.com/KIOS-Research/dbp-virtual-water-testbed/refs/heads/main/Networks/CY-DBP.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-CY-DBP", CYDBP)


@meta_data("network-richmond")
class Richmond(WaterDistributionNetwork):
    """
    Class for loading the Richmond network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Richmond network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Richmond_standard.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Richmond_standard.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "exeter-benchmarks/Richmond_standard.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Richmond", Richmond)


@meta_data("network-micropolis")
class Micropolis(WaterDistributionNetwork):
    """
    Class for loading the Micropolois network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, MICROPOLIS network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the MICROPOLIS_v1.inp file is returned.
        """
        f_in = os.path.join(download_dir, "MICROPOLIS_v1.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/asce-tf-wdst/" + \
            "MICROPOLIS_v1.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Micropolis", Micropolis)


@meta_data("network-balerma")
class Balerma(WaterDistributionNetwork):
    """
    Class for loading the Balerma network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Balerma network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Balerma.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Balerma.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/Balerma.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Balerma", Balerma)


@meta_data("network-rural")
class Rural(WaterDistributionNetwork):
    """
    Class for loading the Rural network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Rural network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the RuralNetwork.inp file is returned.
        """
        f_in = os.path.join(download_dir, "RuralNetwork.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
            "asce-tf-wdst/RuralNetwork.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Rural", Rural)


@meta_data("network-anytown")
class Anytown(WaterDistributionNetwork):
    """
    Class for loading the Anytown network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Anytown network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Anytown.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Anytown.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Anytown.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Anytown", Anytown)


@meta_data("network-dtown")
class DTown(WaterDistributionNetwork):
    """
    Class for loading the D-Town network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, D-Town network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the d-town.inp file is returned.
        """
        f_in = os.path.join(download_dir, "d-town.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/d-town.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-DTown", DTown)


@meta_data("network-ctown")
class CTown(WaterDistributionNetwork):
    """
    Class for loading the C-Town network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, C-Town network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the CTOWN.inp file is returned.
        """
        f_in = os.path.join(download_dir, "CTOWN.INP")
        url = "https://github.com/scy-phy/www.batadal.net/raw/master/data/CTOWN.INP"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-CTown", CTown)


@meta_data("network-hanoi")
class Hanoi(WaterDistributionNetwork):
    """
    Class for loading the Hanoi networks.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             include_default_sensor_placement: bool = False,
             verbose: bool = True, flow_units_id: int = None,
             return_scenario: bool = False) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Hanoi network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Hanoi.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Hanoi.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Hanoi.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            config = load_inp(f_in, flow_units_id=flow_units_id)

            if include_default_sensor_placement is True:
                sensor_config = config.sensor_config
                sensor_config.pressure_sensors = ["13", "16", "22", "30"]
                sensor_config.flow_sensors = ["1"]

                config = ScenarioConfig(scenario_config=config, sensor_config=sensor_config)

            return config
        else:
            return f_in


register("Network-Hanoi", Hanoi)


@meta_data("network-ca1")
class CA1(WaterDistributionNetwork):
    """
    Class for loading the CA1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the CA1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the CA1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "CA1.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1000&context=wdst_us&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-CA1", CA1)


@meta_data("network-etown")
class ETown(WaterDistributionNetwork):
    """
    Class for loading the E-Town network (also called BIWS network).
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the E-Town network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.
            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.
            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.
            Only relevant if 'return_scenario=True'.
            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.
            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the E-Town network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "BIWS.inp")
        url = "https://wdsa-ccwi2022.upv.es/wp-content/uploads/descargas/BIWS.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-ETown", ETown)


@meta_data("network-pa1")
class PA1(WaterDistributionNetwork):
    """
    Class for loading the PA1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the PA1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the PA1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "PA1.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1001&context=wdst_us&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-PA1", PA1)


@meta_data("network-pa2")
class PA2(WaterDistributionNetwork):
    """
    Class for loading the PA2 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the PA2 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the PA2 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "PA2.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1002&context=wdst_us&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-PA2", PA2)


@meta_data("network-wa1")
class WA1(WaterDistributionNetwork):
    """
    Class for loading the WA1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the WA1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the WA1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "WA1.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1003&context=wdst_us&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-WA1", WA1)


@meta_data("network-nj1")
class NJ1(WaterDistributionNetwork):
    """
    Class for loading the NJ1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the NJ1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the NJ1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "NJ1.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1004&context=wdst_us&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-NJ1", NJ1)


@meta_data("network-bwsn1")
class BWSN1(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the BWSN-1 network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "BWSN_Network_1.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
              "asce-tf-wdst/BWSN_Network_1.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-BWSN-1", BWSN1)


@meta_data("network-bwsn2")
class BWSN2(WaterDistributionNetwork):
    """
    Class for loading the BWSN-2 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the BWSN-2 network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "BWSN_Network_2.inp")
        url = "https://github.com/OpenWaterAnalytics/EPyT/raw/main/epyt/networks/" + \
              "asce-tf-wdst/BWSN_Network_2.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-BWSN-2", BWSN2)


@meta_data("network-fossolo")
class Fossolo(WaterDistributionNetwork):
    """
    Class for loading the Fossolo network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Fossolo network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Fossolo network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "Fossolo.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1002&context=wdst_international&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Fossolo", Fossolo)


@meta_data("network-modena")
class Modena(WaterDistributionNetwork):
    """
    Class for loading the Modena network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Modena network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Modena network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "Modena.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1004&context=wdst_international&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Modena", Modena)


@meta_data("network-zhi-jiang")
class ZhiJiang(WaterDistributionNetwork):
    """
    Class for loading the Zhi Jiang network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Zhi Jiang network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Zhi Jiang network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "ZhiJiang.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1005&context=wdst_international&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Zhi-Jiang", ZhiJiang)


@meta_data("network-marchi-rural")
class MarchiRural(WaterDistributionNetwork):
    """
    Class for loading the Marchi Rural network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Marchi Rural network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Marchi Rural network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "MarchiRural.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1006&context=wdst_international&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Marchi-Rural", MarchiRural)


@meta_data("network-ky1")
class KY1(WaterDistributionNetwork):
    """
    Class for loading the KY1 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY1 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY1.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1002&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY1", KY1)


@meta_data("network-ky2")
class KY2(WaterDistributionNetwork):
    """
    Class for loading the KY2 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY2 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY2 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY2.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1003&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY2", KY2)


@meta_data("network-ky3")
class KY3(WaterDistributionNetwork):
    """
    Class for loading the KY3 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY3 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY3 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY3.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1004&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY3", KY3)


@meta_data("network-ky4")
class KY4(WaterDistributionNetwork):
    """
    Class for loading the KY4 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY4 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY4 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY4.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1005&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY4", KY4)


@meta_data("network-ky5")
class KY5(WaterDistributionNetwork):
    """
    Class for loading the KY5 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY5 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY5 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY5.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1006&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY5", KY5)


@meta_data("network-ky6")
class KY6(WaterDistributionNetwork):
    """
    Class for loading the KY6 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY6 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY6 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY6.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1007&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY6", KY6)


@meta_data("network-ky7")
class KY7(WaterDistributionNetwork):
    """
    Class for loading the KY7 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY7 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY7 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY7.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1008&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY7", KY7)


@meta_data("network-ky8")
class KY8(WaterDistributionNetwork):
    """
    Class for loading the KY8 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY8 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY8 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY8.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1009&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY8", KY8)


@meta_data("network-ky9")
class KY9(WaterDistributionNetwork):
    """
    Class for loading the KY9 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY9 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY9 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY9.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1010&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY9", KY9)


@meta_data("network-ky10")
class KY10(WaterDistributionNetwork):
    """
    Class for loading the KY10 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY10 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY10 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY10.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1011&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY10", KY10)


@meta_data("network-ky11")
class KY11(WaterDistributionNetwork):
    """
    Class for loading the KY11 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY11 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY11 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY11.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1012&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY11", KY11)


@meta_data("network-ky12")
class KY12(WaterDistributionNetwork):
    """
    Class for loading the KY12 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY12 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY12 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY12.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1013&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY12", KY12)


@meta_data("network-ky13")
class KY13(WaterDistributionNetwork):
    """
    Class for loading the KY13 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY13 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY13 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY13.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1014&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY13", KY13)


@meta_data("network-ky14")
class KY14(WaterDistributionNetwork):
    """
    Class for loading the KY14 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY14 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY14 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY14.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1015&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY14", KY14)


@meta_data("network-ky15")
class KY15(WaterDistributionNetwork):
    """
    Class for loading the KY15 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY15 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY15 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY15.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1016&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY15", KY15)


@meta_data("network-ky16")
class KY16(WaterDistributionNetwork):
    """
    Class for loading the KY16 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY16 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY16 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY16.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1035&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY16", KY16)


@meta_data("network-ky17")
class KY17(WaterDistributionNetwork):
    """
    Class for loading the KY17 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KY17 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KY17 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KY17.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1036&context=wdst&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KY17", KY17)


@meta_data("network-kyv8")
class KYV8(WaterDistributionNetwork):
    """
    Class for loading the KYV8 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV8 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV8 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV8.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1001&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV8", KYV8)


@meta_data("network-kyv18")
class KYV18(WaterDistributionNetwork):
    """
    Class for loading the KYV18 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV18 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV18 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV18.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1002&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV18", KYV18)


@meta_data("network-kyv21")
class KYV21(WaterDistributionNetwork):
    """
    Class for loading the KYV21 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV21 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV21 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV21.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1005&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV21", KYV21)


@meta_data("network-kyv22")
class KYV22(WaterDistributionNetwork):
    """
    Class for loading the KYV22 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV22 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV22 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV22.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1006&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV22", KYV22)


@meta_data("network-kyv23")
class KYV23(WaterDistributionNetwork):
    """
    Class for loading the KYV23 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV23 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV23 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV23.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1007&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV23", KYV23)


@meta_data("network-kyv24")
class KYV24(WaterDistributionNetwork):
    """
    Class for loading the KYV24 network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KYV24 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KYV24 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KYV24.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1008&context=wdst_ky_valved&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KYV24", KYV24)


@meta_data("network-nyc-tunnel")
class NYC_Tunnel(WaterDistributionNetwork):
    """
    Class for loading the New York City Tunnel network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the New York City Tunnel network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the New York City Tunnel network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "NYC_Tunnel.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=7&article=1000&context=wdst_systems&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-NYC-Tunnel", NYC_Tunnel)


@meta_data("network-nineteen-pipe")
class NineteenPipe(WaterDistributionNetwork):
    """
    Class for loading the nineteen pipe network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the nineteen pipe network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the nineteen pipe network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "NineteenPipe.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1004&context=wdst_systems&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Nineteen-Pipe", NineteenPipe)


@meta_data("network-modified-nineteen-pipe")
class ModifiedNineteenPipe(WaterDistributionNetwork):
    """
    Class for loading the modified nineteen pipe network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the modified nineteen pipe network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the modified nineteen pipe network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "ModifiedNineteenPipe.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1006&context=wdst_systems&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Modified-Nineteen-Pipe", ModifiedNineteenPipe)


@meta_data("network-fowm")
class FOWM(WaterDistributionNetwork):
    """
    Class for loading the FOWM network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the FOWM network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the FOWM network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "FOWM.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1007&context=wdst_systems&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-FOWM", FOWM)


@meta_data("network-fourteen-pipe")
class FourteenPipe(WaterDistributionNetwork):
    """
    Class for loading the Fourteen Pipe network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Fourteen Pipe network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Fourteen Pipe network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "FourteenPipe.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1008&context=wdst_systems&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Fourteen-Pipe", FourteenPipe)


@meta_data("network-kl")
class KL(WaterDistributionNetwork):
    """
    Class for loading the KL network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the KL network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the KL network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "KL.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/asce-tf-wdst/KL.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-KL", KL)


@meta_data("network-jilin")
class Jilin(WaterDistributionNetwork):
    """
    Class for loading the Jilin network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the Jilin network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the Jilin network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "Jilin.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/asce-tf-wdst/Jilin%20including%20water%20quality.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Jilin", Jilin)


@meta_data("network-dma")
class DMA(WaterDistributionNetwork):
    """
    Class for loading the DMA network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the DMA network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the DMA network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "DMA.inp")
        url = "https://uknowledge.uky.edu/cgi/viewcontent.cgi?filename=1&article=1005&context=wdst_models&type=additional"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-DMA", DMA)


@meta_data("network-tln")
class TLN(WaterDistributionNetwork):
    """
    Class for loading the TLN network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the TLN network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the TLN network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "TLN.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/data/3-epanet/TLN.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-TLN", TLN)


@meta_data("network-bak")
class BAK(WaterDistributionNetwork):
    """
    Class for loading the BAK network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the BAK network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the BAK network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "BAK.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/data/3-epanet/BAK.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-BAK", BAK)


@meta_data("network-goy")
class GOY(WaterDistributionNetwork):
    """
    Class for loading the GOY network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the GOY network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the GOY network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "GOY.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/data/3-epanet/GOY.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-GOY", GOY)



@meta_data("network-bin")
class BIN(WaterDistributionNetwork):
    """
    Class for loading the BIN network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the BIN network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the BIN network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "BIN.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/data/3-epanet/BIN.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-BIN", BIN)



@meta_data("network-exn")
class EXN(WaterDistributionNetwork):
    """
    Class for loading the EXN network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the EXN network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the EXN network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "EXN.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/data/3-epanet/EXN.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-EXN", EXN)



@meta_data("network-wcr")
class WCR(WaterDistributionNetwork):
    """
    Class for loading the WCR network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the WCR network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the WCR network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "WCR.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/wolf-initial-fig.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-WCR", WCR)



@meta_data("network-rch")
class RCH(WaterDistributionNetwork):
    """
    Class for loading the RCH network.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the RCH network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the RCH network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_in = os.path.join(download_dir, "RCH.inp")
        url = "https://www.exeter.ac.uk/media/universityofexeter/emps/research/cws/downloads/Richmond_standard.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-RCH", RCH)

