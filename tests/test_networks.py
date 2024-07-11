"""
Module provides tests to test the `water_benchmark_hub.networks.networks` module.
"""
import pytest
from epyt_flow.simulation import ScenarioConfig
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_richmond():
    res = load("Network-Richmond")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_micropolis():
    res = load("Network-Micropolis")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_balerma():
    res = load("Network-Balerma")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_rural():
    res = load("Network-Rural")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_anytown():
    res = load("Network-Anytown")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_dtown():
    res = load("Network-DTown")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ctown():
    res = load("Network-CTown")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_etown():
    res = load("Network-ETown")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_kentucky():
    res = load("Network-Kentucky")

    for i in range(1, 16):
        assert res.load(download_dir=get_temp_folder(), network_id=i) is not None

    with pytest.raises(ValueError):
        res.load(download_dir=get_temp_folder(), network_id=0)

    with pytest.raises(ValueError):
        res.load(download_dir=get_temp_folder(), network_id=16)


def test_hanoi():
    res = load("Network-Hanoi")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True,
                               include_default_sensor_placement=True), ScenarioConfig)
