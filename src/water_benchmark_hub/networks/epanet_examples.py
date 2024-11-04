"""
Module contains the EPANET example networks.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, download_if_necessary

from .networks import WaterDistributionNetwork
from ..meta_data import meta_data
from ..benchmarks import register


@meta_data("network-net1")
class Net1(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 1.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
            `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Net1 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Net1.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net1.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net1.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Net1", Net1)


@meta_data("network-net2")
class Net2(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 2.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
            `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Net2 network loaded into a scenario configuration that can
            be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Net2.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net2.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net2.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Net2", Net2)


@meta_data("network-net3")
class Net3(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 3.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
            `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, Net3 network loaded into a scenario configuration that can
            be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Net3.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net3.inp")
        url = "https://raw.githubusercontent.com/OpenWaterAnalytics/EPyT/main/epyt/networks/" + \
            "asce-tf-wdst/Net3.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Net3", Net3)


@meta_data("network-net6")
class Net6(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 6.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), verbose: bool = True,
             flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
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
            `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True,  Net6 network loaded into a scenario configuration
            that can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the Net6.inp file is returned.
        """
        f_in = os.path.join(download_dir, "Net6.inp")
        url = "https://github.com/OpenWaterAnalytics/WNTR/raw/main/examples/networks/Net6.inp"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


register("Network-Net6", Net6)
