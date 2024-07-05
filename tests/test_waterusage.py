"""
Module provides tests to test the `water_benchmark_hub.water_usage.water_usage` module.
"""
import numpy as np
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_water_usage():
    res = load("KIOS-WaterUsage")

    assert res.get_meta_info() != {}

    # Load as Numpy arrays
    data = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    X, y = data["train"]
    assert X is not None
    assert y is not None

    X, y = data["validation"]
    assert X is not None
    assert y is not None

    X, y = data["test"]
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y) is not None

    # Load as pandas.DataFrame instances
    data = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    df_data = data["train"]
    assert df_data is not None

    df_data = data["validation"]
    assert df_data is not None

    df_data = data["test"]
    assert df_data is not None
