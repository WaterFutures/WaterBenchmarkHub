"""
Module provides tests to test the `water_benchmark_hub.leakdb.leakdb` module.
"""
import json
import numpy as np
from epyt_flow.simulation import ScenarioSimulator
from water_benchmark_hub import load
from water_benchmark_hub.leakdb.leakdb_data import NET1_LEAKAGES

from .utils import get_temp_folder


def test_leakdb_net1():
    res = load("KIOS-LeakDB")

    assert res.get_meta_info() != {}

    configs = res.load_scenarios(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                                 use_net1=True)
    for c in configs:
        with ScenarioSimulator(scenario_config=c) as sim:
            scada_data = sim.run_simulation()
            assert scada_data is not None

    X, y, y_leak_loc = res.load_scada_data(download_dir=get_temp_folder(), scenarios_id=[3],
                                           use_net1=True, return_X_y=True,
                                           return_leak_locations=True)[0]
    assert X is not None
    assert y is not None
    assert y_leak_loc is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5), use_net1=True)
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         use_net1=True, return_X_y=True,
                         return_features_desc=True, return_leak_locations=True)
    assert data is not None


def test_leakdb_hanoi():
    res = load("KIOS-LeakDB")

    assert res.get_meta_info() != {}

    configs = res.load_scenarios(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                                 use_net1=False)
    for c in configs:
        with ScenarioSimulator(scenario_config=c) as sim:
            scada_data = sim.run_simulation()
            assert scada_data is not None

    X, y, y_leak_loc = res.load_scada_data(download_dir=get_temp_folder(), scenarios_id=[3],
                                           use_net1=False, return_X_y=True,
                                           return_leak_locations=True)[0]
    assert X is not None
    assert y is not None
    assert y_leak_loc is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         use_net1=False)
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         use_net1=False, return_X_y=True,
                         return_features_desc=True, return_leak_locations=True)
    assert data is not None


def test_leakdb_evaluation_score():
    res = load("KIOS-LeakDB")
    assert res.get_meta_info() != {}

    # Expected values as computed by the official scoring_algorithm.m.
    # Scenario 3 has two overlapping leaks (counted as one), scenario 9 has two leaks,
    # the second one lasting only 4 time steps.
    scenarios_id = [1, 2, 3, 5, 6, 9]
    n_time_steps = 17520
    leaks_info = json.loads(NET1_LEAKAGES)

    y_true = []
    y_burst = []
    for s_id in scenarios_id:
        y = np.zeros(n_time_steps)
        y_b = np.zeros(n_time_steps)
        for leak in leaks_info[str(s_id)]:
            t_start = int(leak["leak_start_time"])
            y[t_start:int(np.ceil(leak["leak_end_time"]))] = 1
            y_b[t_start:t_start + 10] = 1
        y_true.append(y)
        y_burst.append(y_b)

    # Perfect detector -- the 4 time steps long leak is not detected because only 4 of the
    # 14 time steps in its detection window are alarms
    score = res.compute_evaluation_score(scenarios_id, True, y_true)
    assert score["f1_score"] == 1.
    assert score["true_positive_rate"] == 1.
    assert score["true_negative_rate"] == 1.
    assert abs(score["early_detection_score"] - 6. / 7.) < 1e-10

    # Detector that is delayed by 5 time steps
    y_delayed = [np.concatenate((np.zeros(5), y[:-5])) for y in y_true]
    score = res.compute_evaluation_score(scenarios_id, True, y_delayed)
    assert abs(score["f1_score"] - 0.9985504774897682) < 1e-10
    assert abs(score["true_negative_rate"] - 0.9995836598746082) < 1e-10
    assert abs(score["early_detection_score"] - 0.8511361425430957) < 1e-10

    # Alarms only in the first 10 time steps of each leak
    score = res.compute_evaluation_score(scenarios_id, True, y_burst)
    assert abs(score["f1_score"] - 0.00628823929299796) < 1e-10
    assert score["early_detection_score"] == 0.

    # Alarm in every time step
    score = res.compute_evaluation_score(scenarios_id, True,
                                         [np.ones(n_time_steps) for _ in scenarios_id])
    assert score["true_positive_rate"] == 1.
    assert score["true_negative_rate"] == 0.
    assert score["early_detection_score"] == 1.
