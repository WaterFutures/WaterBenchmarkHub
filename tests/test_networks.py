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


def test_hanoi():
    res = load("Network-Hanoi")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True,
                               include_default_sensor_placement=True), ScenarioConfig)


def test_ca1():
    res = load("Network-CA1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_pa1():
    res = load("Network-PA1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_pa2():
    res = load("Network-PA2")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_wa1():
    res = load("Network-WA1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_nj1():
    res = load("Network-NJ1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_fossolo():
    res = load("Network-Fossolo")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_zhi_jiang():
    res = load("Network-Zhi-Jiang")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_marchi_rural():
    res = load("Network-Marchi-Rural")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky1():
    res = load("Network-KY1")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky2():
    res = load("Network-KY2")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky3():
    res = load("Network-KY3")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky4():
    res = load("Network-KY4")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky5():
    res = load("Network-KY5")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky6():
    res = load("Network-KY6")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky7():
    res = load("Network-KY7")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky8():
    res = load("Network-KY8")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky9():
    res = load("Network-KY9")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky10():
    res = load("Network-KY10")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky11():
    res = load("Network-KY11")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky12():
    res = load("Network-KY12")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky13():
    res = load("Network-KY13")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky14():
    res = load("Network-KY14")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky15():
    res = load("Network-KY15")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky16():
    res = load("Network-KY16")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_ky17():
    res = load("Network-KY17")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_kyv21():
    res = load("Network-KYV21")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_kyv22():
    res = load("Network-KYV22")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)


def test_kyv23():
    res = load("Network-KYV23")

    assert res.get_meta_info() != {}
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)
