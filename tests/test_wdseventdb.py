"""
Module provides tests to test the `water_benchmark_hub.wds_eventdb.wds_eventdb` module.
"""
import numpy as np
from water_benchmark_hub import load
import water_benchmark_hub.wds_eventdb.wds_eventdb

from .utils import get_temp_folder

def test_intaset():
    res = load("WDSEventDB")
    
    assert res.get_meta_info() != {}

    # Load as Numpy arrays
    X, y = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    assert X is not None
    assert y is not None
    assert len(X) == len(y)

    # Load as pandas.DataFrame instances
    data = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    
    assert data is not None
    assert "clean" in data
    assert "cyberattack" in data
    assert "leakage" in data
    assert "sensor_failure" in data
