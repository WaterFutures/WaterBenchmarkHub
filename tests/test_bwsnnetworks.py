"""
Module provides tests to test the `water_benchmark_hub.networks.bwsn_networks` module.
"""
from epyt_flow.simulation import ScenarioConfig
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_bwsn1():
    res = load("Network-BWSN1")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_bwsn2():
    res = load("Network-BWSN2")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)
