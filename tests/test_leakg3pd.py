"""
Module provides tests to test the `water_benchmark_hub.leakg3pd.leakg3pd` module.
"""
from epyt_flow.simulation import ScenarioSimulator
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_leakg3pd_net1():
    res = load("LeakG3PD")

    assert res.get_meta_info() != {}

    configs = res.load_scenarios(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                                 network="net1")
    for c in configs:
        with ScenarioSimulator(scenario_config=c) as sim:
            scada_data = sim.run_simulation()
            assert scada_data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5), network="net1")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         network="net1", return_X_y=True,
                         return_features_desc=True, return_leak_locations=True)
    assert data is not None


def test_leakg3pd_net3():
    res = load("LeakG3PD")

    assert res.get_meta_info() != {}

    configs = res.load_scenarios(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                                 network="net3")
    for c in configs:
        with ScenarioSimulator(scenario_config=c) as sim:
            scada_data = sim.run_simulation()
            assert scada_data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5), network="net3")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         network="net3", return_X_y=True,
                         return_features_desc=True, return_leak_locations=True)
    assert data is not None


def test_leakg3pd_hanoi():
    res = load("LeakG3PD")

    assert res.get_meta_info() != {}

    configs = res.load_scenarios(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                                 network="hanoi")
    for c in configs:
        with ScenarioSimulator(scenario_config=c) as sim:
            scada_data = sim.run_simulation()
            assert scada_data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5), network="hanoi")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), scenarios_id=range(1, 5),
                         network="hanoi", return_X_y=True,
                         return_features_desc=True, return_leak_locations=True)
    assert data is not None
