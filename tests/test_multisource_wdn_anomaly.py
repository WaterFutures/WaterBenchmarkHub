"""
Module provides tests to test the `water_benchmark_hub.multisource_wdn_anomaly.multisource_wdn_anomaly` module.
"""
import numpy as np
from water_benchmark_hub import load
import water_benchmark_hub.multisource_wdn_anomaly.multisource_wdn_anomaly

from .utils import get_temp_folder

def test_multisource_wdn_anomaly():
    from water_benchmark_hub import load

    res = load("MultiSourceWDNAnomaly")
    assert res.get_meta_info() != {}

    # Load as Numpy arrays
    X, y = res.load_data(download_dir=get_temp_folder(), return_X_y=True)
    assert X is not None
    assert y is not None
    assert len(X) == len(y)
    assert X.shape[1] == 18   # 20 columns - timestamp - fault_d7

    # Load as pandas.DataFrame
    df = res.load_data(download_dir=get_temp_folder(), return_X_y=False)
    assert df is not None
    assert "timestamp" in df
    assert "fault_d7" in df
    assert len(df) == len(X)