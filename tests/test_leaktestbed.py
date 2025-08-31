"""
Module provides tests to test the `water_benchmark_hub.leak_testbed.leak_testbed` module.
"""
from water_benchmark_hub import load
from water_benchmark_hub.leak_testbed import LeakType, Demand

from .utils import get_temp_folder


def test_leaktestbed_branched():
    res = load("LeakTestbed")

    assert res.get_meta_info() != {}

    data = res.load_data(download_dir=get_temp_folder(), network="branched")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), network="branched",
                         leak_types=(LeakType.GASKET_LEAK, LeakType.ORIFICE_LEAK), demands=Demand.LARGE)
    assert data is not None


def test_leaktestbed_looped():
    res = load("LeakTestbed")

    data = res.load_data(download_dir=get_temp_folder(), network="looped")
    assert data is not None

    data = res.load_data(download_dir=get_temp_folder(), network="looped",
                         leak_types=4, demands=(2, 3))
    assert data is not None
