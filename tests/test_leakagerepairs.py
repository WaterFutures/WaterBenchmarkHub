"""
Module provides tests to test the `water_benchmark_hub.leakage_repairs.leakage_repairs` module.
"""
from water_benchmark_hub import load
import water_benchmark_hub.leakage_repairs.leakage_repairs
import pandas as pd

from .utils import get_temp_folder

def test_intaset():
    res = load("KIOS-LeakageRepairs")
    
    assert res.get_meta_info() != {}



    # Load as pandas.DataFrame instances
    data = res.load_data(download_dir=get_temp_folder())

    assert data is not None

    assert isinstance(data, dict)
    assert "reports" in data
    assert "flow" in data

    assert isinstance(data["reports"], pd.DataFrame)
    assert isinstance(data["flow"], dict)

    for area, df in data["flow"].items():
        assert isinstance(df, pd.DataFrame)