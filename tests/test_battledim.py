"""
Module provides tests to test the `water_benchmark_hub.battledim.battledim` module.
"""
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_battledim():
    res = load("BattLeDIM")

    assert res.get_meta_info() != {}

    hist_scenario = res.load_scenario(download_dir=get_temp_folder(), return_test_scenario=False)
    assert hist_scenario is not None

    eval_scenario = res.load_scenario(download_dir=get_temp_folder(), return_test_scenario=True)
    assert eval_scenario is not None
