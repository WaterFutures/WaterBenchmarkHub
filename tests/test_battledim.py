"""
Module provides tests to test the `water_benchmark_hub.battledim.battledim` module.
"""
from datetime import datetime
from water_benchmark_hub import load
from water_benchmark_hub.battledim.battledim_data import LEAKS_CONFIG_TEST, START_TIME_TEST

from .utils import get_temp_folder


def test_battledim():
    res = load("BattLeDIM")

    assert res.get_meta_info() != {}

    hist_scenario = res.load_scenario(download_dir=get_temp_folder(), return_test_scenario=False)
    assert hist_scenario is not None

    eval_scenario = res.load_scenario(download_dir=get_temp_folder(), return_test_scenario=True)
    assert eval_scenario is not None


def test_battledim_evaluation_score():
    res = load("BattLeDIM")
    assert res.get_meta_info() != {}

    # One alarm on each leaky pipe at the start of its leak
    perfect_alarms = []
    for leak in LEAKS_CONFIG_TEST.splitlines():
        items = [i.strip() for i in leak.split(",")]
        start_time = (datetime.strptime(items[1], "%Y-%m-%d %H:%M") - START_TIME_TEST)
        perfect_alarms.append((items[0], int(start_time.total_seconds())))

    # As in the official PERFECT_TEAM_report.txt: EUR 523,153.82 with 23 true positives
    score = res.compute_evaluation_score(perfect_alarms, test_scenario=True)
    assert score["true_positives"] == 23 and score["false_positives"] == 0
    assert abs(score["total_savings"] - 523153.82) < .01

    # Repeated detections are ignored
    score = res.compute_evaluation_score(perfect_alarms + perfect_alarms,
                                         test_scenario=True)
    assert score["true_positives"] == 23 and score["false_positives"] == 0
    assert abs(score["total_savings"] - 523153.82) < .01

    # An alarm more than 300m away from all leaks is a false positive
    score = res.compute_evaluation_score([("p227", 3600)], test_scenario=True)
    assert score["true_positives"] == 0 and score["false_positives"] == 1
    assert score["total_savings"] == -500.
