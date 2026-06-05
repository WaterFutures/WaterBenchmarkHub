"""
Module contains the EPANET example networks.
"""
from .networks import WaterDistributionNetwork
from ..meta_data import meta_data
from ..benchmarks import register


@meta_data("network-net1")
class Net1(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 1.
    """
    pass


register("Network-Net1", Net1)


@meta_data("network-net2")
class Net2(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 2.
    """
    pass


register("Network-Net2", Net2)


@meta_data("network-net3")
class Net3(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 3.
    """
    pass


register("Network-Net3", Net3)


@meta_data("network-net6")
class Net6(WaterDistributionNetwork):
    """
    Class for loading the EPANET Example Network 6.
    """
    pass


register("Network-Net6", Net6)
