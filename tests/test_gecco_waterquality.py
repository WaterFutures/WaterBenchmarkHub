"""
Module provides tests to test the `water_benchmark_hub.gecco_waterquality.gecco_waterquality` module.
"""
import numpy as np
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_gecco_waterquality2017():
    res = load("GECCO-WaterQuality2017")

    assert res.get_meta_info() != {}

    X, y = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y=y) is not None

    df_data = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    assert df_data is not None


def test_gecco_waterquality2018():
    res = load("GECCO-WaterQuality2018")

    assert res.get_meta_info() != {}

    X, y = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y=y) is not None

    df_data = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    assert df_data is not None


def test_gecco_waterquality2019():
    res = load("GECCO-WaterQuality2019")

    assert res.get_meta_info() != {}

    d = res.load_data(download_dir=get_temp_folder(), return_X_y=True)

    X, y = d["train"]
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y=y) is not None

    X, y = d["validation"]
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y=y) is not None

    X, y = d["test"]
    assert X is not None
    assert y is not None
    assert res.compute_evaluation_score(np.random.choice([0, 1], size=y.shape), y=y) is not None

    df_data = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    assert df_data is not None
