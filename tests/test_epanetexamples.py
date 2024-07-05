"""
Module provides tests to test the `water_benchmark_hub.networks.epanet_examples` module.
"""
from epyt_flow.simulation import ScenarioConfig
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_net1():
    res = load("Network-Net1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_net2():
    res = load("Network-Net2")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_net3():
    res = load("Network-Net3")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_net6():
    res = load("Network-Net6")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)
