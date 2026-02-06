"""
Module provides tests to test the `water_benchmark_hub.ditec_wdn.ditec_wdn` module.
"""
from water_benchmark_hub import load

from .utils import get_temp_folder


def test_ditec_wdn_small():
    res = load("DiTEC-WDN")

    data = res.load_data(download_dir=get_temp_folder(), network="exn")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), network="ctown",
                         scenarios_id=[1, 2, 3])
    assert data is not None
