"""
Module contains the BWSN networks.
"""
from .networks import WaterDistributionNetwork
from ..meta_data import meta_data
from ..benchmarks import register


@meta_data("network-bwsn1")
class BWSN1(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    pass


register("Network-BWSN1", BWSN1)


@meta_data("network-bwsn2")
class BWSN2(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    pass


register("Network-BWSN2", BWSN2)
