"""
Module provides tests to test the `water_benchmark_hub.leakdb.leakdb` module.
"""
from epyt_flow.simulation import ScenarioSimulator
from water_benchmark_hub import load

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
