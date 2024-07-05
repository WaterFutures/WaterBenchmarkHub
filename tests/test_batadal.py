"""
Module provides tests to test the `water_benchmark_hub.batadal.batadal` module.
"""
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_batadal():
    res = load("BATADAL")

    assert res.get_meta_info() != {}

    data = res.load_data(download_dir=get_temp_folder())
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), return_X_y=True,
                         return_ground_truth=True)
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), return_X_y=True,
                         return_ground_truth=True, return_features_desc=True)
    assert data is not None
