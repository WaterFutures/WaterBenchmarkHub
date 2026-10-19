"""
Module provides tests to test the `water_benchmark_hub.clstateestimate.clstateestimate` module.
"""
import os
import subprocess
import sys

import numpy as np

import water_benchmark_hub
from water_benchmark_hub.clstateestimate.clstateestimate import ChlorineStateEstimation


def _write_scenario(folder, s_id, n_time_steps=3, n_nodes=4, n_flows=2):
    """
    Writes a minimal scenario file (npz) mimicking the data set of the
    Chlorine State Estimation benchmark.

    Parameters
    ----------
    folder : `str`
        Directory the scenario file is written to.
    s_id : `int`
        ID of the scenario -- it is used as scenario marker within the data.
    n_time_steps : `int`, optional
        Number of time steps of the scenario.
    n_nodes : `int`, optional
        Number of nodes of the network.
    n_flows : `int`, optional
        Number of flow measurements per time step.
    """
    np.savez(os.path.join(folder, f"{s_id}.npz"),
             node_ids=np.array([str(i) for i in range(1, n_nodes + 1)]),
             flow_data=np.full((n_time_steps, n_flows), float(s_id)),
             node_quality=np.full((n_time_steps, n_nodes), float(s_id)),
             injection_node_id=np.array(["1"]))


def test_clstateestimate_is_registered():
    # The benchmark has to be reachable through the public API. A fresh
    # interpreter is used here, so that the result does not depend on the
    # import order of the test session.
    code = ("from water_benchmark_hub import load; "
            "assert load('ClStateEstimate') is not None")
    env = os.environ.copy()
    pkg_root = os.path.dirname(os.path.dirname(water_benchmark_hub.__file__))
    env["PYTHONPATH"] = os.pathsep.join(
        [p for p in (pkg_root, env.get("PYTHONPATH", "")) if p])

    res = subprocess.run([sys.executable, "-c", code], env=env,
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stderr


def test_clstateestimate_train_val_test_split(tmp_path, monkeypatch):
    n_scenarios = 5
    train_size = 2
    val_size = 1

    data_dir = os.path.join(
        tmp_path, "chlorine-data", "Net1", "randomized_demands=False-spike")
    os.makedirs(data_dir)
    for s_id in range(n_scenarios):
        _write_scenario(data_dir, s_id)

    # The scenarios are created above -- hence, no download is needed
    monkeypatch.setattr(
        ChlorineStateEstimation, "_download_and_extract",
        staticmethod(lambda *args, **kwargs: None))

    res = ChlorineStateEstimation()
    splits = res.load_data(
        download_dir=str(tmp_path), net_desc="Net1", target_node_id="2",
        train_size=train_size, val_size=val_size, shuffle=False)

    def scenario_ids(X):
        """Returns the IDs of the scenarios the given data blocks belong to."""
        return [int(scenario[0][0]) for scenario in X]

    X_train, y_train = splits["train"]
    X_val, y_val = splits["val"]
    X_test, y_test = splits["test"]

    assert len(X_train) == train_size
    assert len(y_train) == train_size
    assert len(X_val) == val_size
    assert len(y_val) == val_size
    # The test split must contain the scenarios that are in neither the train
    # nor in the validation split
    assert len(X_test) == n_scenarios - train_size - val_size
    assert len(y_test) == n_scenarios - train_size - val_size

    assert scenario_ids(X_train) == [0, 1]
    assert scenario_ids(X_val) == [2]
    assert scenario_ids(X_test) == [3, 4]
