"""
Module contains the L-Town network.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, download_if_necessary

from .networks import WaterDistributionNetwork
from ..meta_data import meta_data
from ..benchmarks import register


@meta_data("network-ltown")
class LTown(WaterDistributionNetwork):
    """
    Class for loading the L-Town networks.
    """
    @staticmethod
    def load(download_dir: str = get_temp_folder(), use_realistic_demands: bool = False,
             include_default_sensor_placement: bool = False,
             verbose: bool = True, flow_units_id: int = None, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the L-TOWN_v2 network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        use_realistic_demands : `bool`, optional
            If True, realistic demands from the BattLeDIM challenge will be included,
            toy demands will be included otherwise.

            The default is False
        include_default_sensor_placement : `bool`, optional
            If True, the L-TOWN default sensor placement will be included
            in the returned scenario configuration.

            The default is False
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

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
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, L-TOWN_v2 network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_inp = "L-TOWN_v2_Model.inp" if use_realistic_demands is False else "L-TOWN_v2_Real.inp"

        f_in = os.path.join(download_dir, f_inp)
        if not use_realistic_demands:
            url = "https://zenodo.org/records/4017659/files/L-TOWN.inp?download=1"
        else:
            url = "https://zenodo.org/records/4017659/files/L-TOWN_Real.inp?download=1"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            config = load_inp(f_in, flow_units_id=flow_units_id)

            if include_default_sensor_placement is True:
                sensor_config = config.sensor_config
                sensor_config.pressure_sensors = ["n54", "n105", "n114", "n163", "n188", "n229", "n288",
                                                "n296", "n332", "n342", "n410", "n415", "n429", "n458",
                                                "n469", "n495", "n506", "n516", "n519", "n549", "n613",
                                                "n636", "n644", "n679", "n722", "n726", "n740", "n752",
                                                "n769"]
                sensor_config.flow_sensors = ["p227", "p235"]
                sensor_config.tank_volume_sensors = ["T1"]
                sensor_config.demand_sensors = ["n1", "n2",	"n3", "n4", "n6", "n7",	"n8", "n9",	"n10",
                                                "n11", "n13", "n16", "n17", "n18", "n19", "n20", "n21",
                                                "n22",	"n23", "n24", "n25", "n26", "n27", "n28", "n29",
                                                "n30", "n31", "n32", "n33",	"n34", "n35", "n36", "n39",
                                                "n40", "n41", "n42", "n43",	"n44", "n45", "n343", "n344",
                                                "n345",	"n346",	"n347",	"n349",	"n350",	"n351",	"n352",
                                                "n353",	"n354",	"n355",	"n356",	"n357",	"n358",	"n360",
                                                "n361",	"n362",	"n364",	"n365",	"n366",	"n367", "n368",
                                                "n369",	"n370",	"n371",	"n372",	"n373",	"n374", "n375",
                                                "n376",	"n377",	"n378", "n379",	"n381",	"n382",	"n383",
                                                "n384",	"n385",	"n386", "n387",	"n388",	"n389"]

                config = ScenarioConfig(scenario_config=config, sensor_config=sensor_config)

            return config
        else:
            return f_in

    @staticmethod
    def load_ltown_a(download_dir: str = get_temp_folder(), use_realistic_demands: bool = False,
                     include_default_sensor_placement: bool = False,
                     verbose: bool = True, flow_units_id: int = None, return_scenario: bool = False
                     ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the L-TOWN-A network (area "A" of the L-TOWN network).

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        use_realistic_demands : `bool`, optional
            If True, realistic demands from the BattLeDIM challenge will be included,
            toy demands will be included otherwise.

            The default is False
        include_default_sensor_placement : `bool`, optional
            If True, the L-TOWN default sensor placement will be included
            in the returned scenario configuration.

            The default is False
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

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
        `epyt_flow.simulation.scenario_config.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, L-TOWN-A network loaded into a scenario configuration that
            can be passed on to `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        f_inp = "L-TOWN_v2-A_Model.inp" if use_realistic_demands is False else "L-TOWN_v2-A_Real.inp"

        f_in = os.path.join(download_dir, f_inp)
        url = f"https://filedn.com/lumBFq2P9S74PNoLPWtzxG4/EPyT-Flow/Networks/{f_inp}"

        download_if_necessary(f_in, url, verbose)

        if return_scenario is True:
            config = load_inp(f_in, flow_units_id=flow_units_id)

            if include_default_sensor_placement is True:
                sensor_config = config.sensor_config
                sensor_config.pressure_sensors = ["n54", "n105", "n114", "n163", "n188", "n229", "n288",
                                                "n296", "n332", "n342", "n410", "n415", "n429", "n458",
                                                "n469", "n495", "n506", "n516", "n519", "n549", "n613",
                                                "n636", "n644", "n679", "n722", "n726", "n740", "n752",
                                                "n769"]
                sensor_config.flow_sensors = ["p227", "p235"]

                config = ScenarioConfig(scenario_config=config, sensor_config=sensor_config)

            return config
        else:
            return f_in


register("Network-LTown", LTown)
