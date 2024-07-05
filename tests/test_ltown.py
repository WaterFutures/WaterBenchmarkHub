"""
Module provides tests to test the `water_benchmark_hub.networks.ltown` module.
"""
from epyt_flow.simulation import ScenarioConfig
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_ltown():
    res = load("Network-LTown")

    assert res.get_meta_info() != {}

    # Entire L-Town
    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)

    assert isinstance(res.load(download_dir=get_temp_folder(), use_realistic_demands=True), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True,
                               use_realistic_demands=True), ScenarioConfig)

    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True,
                               use_realistic_demands=True,
                               include_default_sensor_placement=True), ScenarioConfig)

    # L-Town Area A
    assert isinstance(res.load_ltown_a(download_dir=get_temp_folder()), str)
    assert isinstance(res.load_ltown_a(download_dir=get_temp_folder(), return_scenario=True),
                      ScenarioConfig)

    assert isinstance(res.load_ltown_a(download_dir=get_temp_folder(), use_realistic_demands=True),
                      str)
    assert isinstance(res.load_ltown_a(download_dir=get_temp_folder(), return_scenario=True,
                                       use_realistic_demands=True), ScenarioConfig)

    assert isinstance(res.load_ltown_a(download_dir=get_temp_folder(), return_scenario=True,
                                       use_realistic_demands=True,
                                       include_default_sensor_placement=True), ScenarioConfig)
