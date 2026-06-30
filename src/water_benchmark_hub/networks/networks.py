"""
Module provides functions for loading different water distribution networks.
"""
from typing import Union
import os

from epyt_flow.data.networks import load_inp
from epyt_flow.simulation import ScenarioConfig
from epyt_flow.utils import get_temp_folder, robust_download

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


class WaterDistributionNetwork(BenchmarkResource):
    """
    Base class of water distribution networks.
    """
    def get_meta_info(self) -> dict:
        raise NotImplementedError()

    def load(self, download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True, return_scenario: bool = False
             ) -> Union[ScenarioConfig, str]:
        """
        Loads (and downloads if necessary) the network.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the directory where the .inp file is stored.

            The default is the OS-specific temporary directory (e.g. "C:\\\\temp", "/tmp/", etc.)
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading the file.

            The default is True.
        flow_units_id : `int`, optional
            Specifies the flow units to be used in this scenario.
            If None, the units from the .inp file will be used.

            Only relevant if 'return_scenario=True'.

            Must be one of the following EPANET toolkit constants:

                - EN_CFS  = 0  (cubic foot/sec)
                - EN_GPM  = 1  (gal/min)
                - EN_MGD  = 2  (Million gal/day)
                - EN_IMGD = 3  (Imperial MGD)
                - EN_AFD  = 4  (ac-foot/day)
                - EN_LPS  = 5  (liter/sec)
                - EN_LPM  = 6  (liter/min)
                - EN_MLD  = 7  (Megaliter/day)
                - EN_CMH  = 8  (cubic meter/hr)
                - EN_CMD  = 9  (cubic meter/day)
                - EN_CMS  = 10 (cubic meters per second)

            The default is None.
        return_scenario : `bool`, optional
            If True, the network is returned as a
            `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ instance.
            Otherwise, the path to the .inp file is returned as a string.

            The default is False.

        Returns
        -------
        `epyt_flow.simulation.ScenarioConfig <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_config.ScenarioConfig>`_ or `str`
            If `return_scenario` is True, the network loaded into a scenario configuration that
            can be passed on to
            `epyt_flow.simulation.scenario_simulator.ScenarioSimulator <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.simulation.html#epyt_flow.simulation.scenario_simulator.ScenarioSimulator>`_.
            Otherwise, the path to the .inp file is returned.
        """
        meta_info = self.get_meta_info()
        urls = [meta_info["download_url"]]
        if "backup_download_urls" in meta_info:
            urls += meta_info["backup_download_urls"]

        f_in = os.path.join(download_dir, f"{self.__class__.__name__}.inp")
        robust_download(f_in, urls, verbose)

        if return_scenario is True:
            return load_inp(f_in, flow_units_id=flow_units_id)
        else:
            return f_in


@meta_data("network-cy-dbp")
class CYDBP(WaterDistributionNetwork):
    """
    Class for loading the CY-DBP network.
    """
    pass


register("Network-CY-DBP", CYDBP)


@meta_data("network-richmond")
class Richmond(WaterDistributionNetwork):
    """
    Class for loading the Richmond network.
    """
    pass


register("Network-Richmond", Richmond)


@meta_data("network-micropolis")
class Micropolis(WaterDistributionNetwork):
    """
    Class for loading the Micropolois network.
    """
    pass


register("Network-Micropolis", Micropolis)


@meta_data("network-balerma")
class Balerma(WaterDistributionNetwork):
    """
    Class for loading the Balerma network.
    """
    pass


register("Network-Balerma", Balerma)


@meta_data("network-rural")
class Rural(WaterDistributionNetwork):
    """
    Class for loading the Rural network.
    """
    pass


register("Network-Rural", Rural)


@meta_data("network-anytown")
class Anytown(WaterDistributionNetwork):
    """
    Class for loading the Anytown network.
    """
    pass


register("Network-Anytown", Anytown)


@meta_data("network-dtown")
class DTown(WaterDistributionNetwork):
    """
    Class for loading the D-Town network.
    """
    pass


register("Network-DTown", DTown)


@meta_data("network-ctown")
class CTown(WaterDistributionNetwork):
    """
    Class for loading the C-Town network.
    """
    pass


register("Network-CTown", CTown)


@meta_data("network-hanoi")
class Hanoi(WaterDistributionNetwork):
    """
    Class for loading the Hanoi networks.
    """
    pass


register("Network-Hanoi", Hanoi)


@meta_data("network-ca1")
class CA1(WaterDistributionNetwork):
    """
    Class for loading the CA1 network.
    """
    pass


register("Network-CA1", CA1)


@meta_data("network-etown")
class ETown(WaterDistributionNetwork):
    """
    Class for loading the E-Town network (also called BIWS network).
    """
    pass


register("Network-ETown", ETown)


@meta_data("network-pa1")
class PA1(WaterDistributionNetwork):
    """
    Class for loading the PA1 network.
    """
    pass


register("Network-PA1", PA1)


@meta_data("network-pa2")
class PA2(WaterDistributionNetwork):
    """
    Class for loading the PA2 network.
    """
    pass


register("Network-PA2", PA2)


@meta_data("network-wa1")
class WA1(WaterDistributionNetwork):
    """
    Class for loading the WA1 network.
    """
    pass


register("Network-WA1", WA1)


@meta_data("network-nj1")
class NJ1(WaterDistributionNetwork):
    """
    Class for loading the NJ1 network.
    """
    pass


register("Network-NJ1", NJ1)


@meta_data("network-bwsn1")
class BWSN1(WaterDistributionNetwork):
    """
    Class for loading the BWSN-1 network.
    """
    pass


register("Network-BWSN-1", BWSN1)


@meta_data("network-bwsn2")
class BWSN2(WaterDistributionNetwork):
    """
    Class for loading the BWSN-2 network.
    """
    pass


register("Network-BWSN-2", BWSN2)


@meta_data("network-fossolo")
class Fossolo(WaterDistributionNetwork):
    """
    Class for loading the Fossolo network.
    """
    pass


register("Network-Fossolo", Fossolo)


@meta_data("network-modena")
class Modena(WaterDistributionNetwork):
    """
    Class for loading the Modena network.
    """
    pass


register("Network-Modena", Modena)


@meta_data("network-zhi-jiang")
class ZhiJiang(WaterDistributionNetwork):
    """
    Class for loading the Zhi Jiang network.
    """
    pass


register("Network-Zhi-Jiang", ZhiJiang)


@meta_data("network-marchi-rural")
class MarchiRural(WaterDistributionNetwork):
    """
    Class for loading the Marchi Rural network.
    """
    pass


register("Network-Marchi-Rural", MarchiRural)


@meta_data("network-ky1")
class KY1(WaterDistributionNetwork):
    """
    Class for loading the KY1 network.
    """
    pass


register("Network-KY1", KY1)


@meta_data("network-ky2")
class KY2(WaterDistributionNetwork):
    """
    Class for loading the KY2 network.
    """
    pass


register("Network-KY2", KY2)


@meta_data("network-ky3")
class KY3(WaterDistributionNetwork):
    """
    Class for loading the KY3 network.
    """
    pass


register("Network-KY3", KY3)


@meta_data("network-ky4")
class KY4(WaterDistributionNetwork):
    """
    Class for loading the KY4 network.
    """
    pass


register("Network-KY4", KY4)


@meta_data("network-ky5")
class KY5(WaterDistributionNetwork):
    """
    Class for loading the KY5 network.
    """
    pass


register("Network-KY5", KY5)


@meta_data("network-ky6")
class KY6(WaterDistributionNetwork):
    """
    Class for loading the KY6 network.
    """
    pass


register("Network-KY6", KY6)


@meta_data("network-ky7")
class KY7(WaterDistributionNetwork):
    """
    Class for loading the KY7 network.
    """
    pass


register("Network-KY7", KY7)


@meta_data("network-ky8")
class KY8(WaterDistributionNetwork):
    """
    Class for loading the KY8 network.
    """
    pass


register("Network-KY8", KY8)


@meta_data("network-ky9")
class KY9(WaterDistributionNetwork):
    """
    Class for loading the KY9 network.
    """
    pass


register("Network-KY9", KY9)


@meta_data("network-ky10")
class KY10(WaterDistributionNetwork):
    """
    Class for loading the KY10 network.
    """
    pass


register("Network-KY10", KY10)


@meta_data("network-ky11")
class KY11(WaterDistributionNetwork):
    """
    Class for loading the KY11 network.
    """
    pass


register("Network-KY11", KY11)


@meta_data("network-ky12")
class KY12(WaterDistributionNetwork):
    """
    Class for loading the KY12 network.
    """
    pass


register("Network-KY12", KY12)


@meta_data("network-ky13")
class KY13(WaterDistributionNetwork):
    """
    Class for loading the KY13 network.
    """
    pass


register("Network-KY13", KY13)


@meta_data("network-ky14")
class KY14(WaterDistributionNetwork):
    """
    Class for loading the KY14 network.
    """
    pass


register("Network-KY14", KY14)


@meta_data("network-ky15")
class KY15(WaterDistributionNetwork):
    """
    Class for loading the KY15 network.
    """
    pass


register("Network-KY15", KY15)


@meta_data("network-ky16")
class KY16(WaterDistributionNetwork):
    """
    Class for loading the KY16 network.
    """
    pass


register("Network-KY16", KY16)


@meta_data("network-ky17")
class KY17(WaterDistributionNetwork):
    """
    Class for loading the KY17 network.
    """
    pass


register("Network-KY17", KY17)


@meta_data("network-kyv8")
class KYV8(WaterDistributionNetwork):
    """
    Class for loading the KYV8 network.
    """
    pass


register("Network-KYV8", KYV8)


@meta_data("network-kyv18")
class KYV18(WaterDistributionNetwork):
    """
    Class for loading the KYV18 network.
    """
    pass


register("Network-KYV18", KYV18)


@meta_data("network-kyv21")
class KYV21(WaterDistributionNetwork):
    """
    Class for loading the KYV21 network.
    """
    pass


register("Network-KYV21", KYV21)


@meta_data("network-kyv22")
class KYV22(WaterDistributionNetwork):
    """
    Class for loading the KYV22 network.
    """
    pass


register("Network-KYV22", KYV22)


@meta_data("network-kyv23")
class KYV23(WaterDistributionNetwork):
    """
    Class for loading the KYV23 network.
    """
    pass


register("Network-KYV23", KYV23)


@meta_data("network-kyv24")
class KYV24(WaterDistributionNetwork):
    """
    Class for loading the KYV24 network.
    """
    pass


register("Network-KYV24", KYV24)


@meta_data("network-nyc-tunnel")
class NYC_Tunnel(WaterDistributionNetwork):
    """
    Class for loading the New York City Tunnel network.
    """
    pass


register("Network-NYC-Tunnel", NYC_Tunnel)


@meta_data("network-nineteen-pipe")
class NineteenPipe(WaterDistributionNetwork):
    """
    Class for loading the nineteen pipe network.
    """
    pass


register("Network-Nineteen-Pipe", NineteenPipe)


@meta_data("network-modified-nineteen-pipe")
class ModifiedNineteenPipe(WaterDistributionNetwork):
    """
    Class for loading the modified nineteen pipe network.
    """
    pass


register("Network-Modified-Nineteen-Pipe", ModifiedNineteenPipe)


@meta_data("network-fowm")
class FOWM(WaterDistributionNetwork):
    """
    Class for loading the FOWM network.
    """
    pass


register("Network-FOWM", FOWM)


@meta_data("network-fourteen-pipe")
class FourteenPipe(WaterDistributionNetwork):
    """
    Class for loading the Fourteen Pipe network.
    """
    pass


register("Network-Fourteen-Pipe", FourteenPipe)


@meta_data("network-kl")
class KL(WaterDistributionNetwork):
    """
    Class for loading the KL network.
    """
    pass


register("Network-KL", KL)


@meta_data("network-jilin")
class Jilin(WaterDistributionNetwork):
    """
    Class for loading the Jilin network.
    """
    pass


register("Network-Jilin", Jilin)


@meta_data("network-dma")
class DMA(WaterDistributionNetwork):
    """
    Class for loading the DMA network.
    """
    pass


register("Network-DMA", DMA)


@meta_data("network-trn")
class TRN(WaterDistributionNetwork):
    """
    Class for loading the Two-Reservoir network (TRN).
    """
    pass


register("Network-TRN", TRN)


@meta_data("network-tln")
class TLN(WaterDistributionNetwork):
    """
    Class for loading the Two-Loop Network (TLN).
    """
    pass


register("Network-TLN", TLN)


@meta_data("network-bak")
class BAK(WaterDistributionNetwork):
    """
    Class for loading the BAK network.
    """
    pass


register("Network-BAK", BAK)


@meta_data("network-goy")
class GOY(WaterDistributionNetwork):
    """
    Class for loading the GOY network.
    """
    pass


register("Network-GOY", GOY)



@meta_data("network-bin")
class BIN(WaterDistributionNetwork):
    """
    Class for loading the BIN network.
    """
    pass


register("Network-BIN", BIN)



@meta_data("network-exn")
class EXN(WaterDistributionNetwork):
    """
    Class for loading the EXN network.
    """
    pass


register("Network-EXN", EXN)



@meta_data("network-wcr")
class WCR(WaterDistributionNetwork):
    """
    Class for loading the WCR network.
    """
    pass


register("Network-WCR", WCR)



@meta_data("network-rch")
class RCH(WaterDistributionNetwork):
    """
    Class for loading the RCH network.
    """
    pass


register("Network-RCH", RCH)
