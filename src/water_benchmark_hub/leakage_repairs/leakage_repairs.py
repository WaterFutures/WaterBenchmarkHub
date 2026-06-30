"""
Model provides access to the KIOS Leakage-Repairs-Dataset benchmark. 
"""
import os
import pandas as pd

from epyt_flow.utils import create_path_if_not_exist, download_if_necessary, get_temp_folder

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data

#***********************************************************
# Constants 
#***********************************************************
_BASE_URL = "https://raw.githubusercontent.com/KIOS-Research/Leakage-Repairs-Dataset/refs/heads/main/data/"

_REPORTS_URL = _BASE_URL + "processed_reports_data/leak_reports.csv"

_AREAS = ["Area_1", "Area_2", "Area_3", "Area_4", "Area_5", "Area_6"]


_FLOW_URLS = {
    area: _BASE_URL + f"raw_flow_data/{area}.csv" 
    for area in _AREAS
}


_REPORTS_COLUMNS = ["topic", "reason", "action", "area", "timestamp", "severity", "repeated"]

_FLOW_COLUMNS = ["result_time", "Flow"]


#***********************************************************
# Class 
#***********************************************************
@meta_data("KIOS-LeakageRepairs")
class LeakageRepairs(BenchmarkResource): 

    """
    The **Leakage-Repairs-Dataset** benchmark by KIOS Research and 
    Innovation Centre of Excellence, University of Cyprus.

    This dataset contains real-world data collected from a water
    distribution network in Cyprus, covering:

    - **Leak reports**: field repair reports (``leak_reports.csv``) with columns ``topic`` (Greek-language event category), ``reason``, ``action``, ``area`` (``Area_1`` - ``Area_6``), ``timestamp``, ``severity`` (``Low`` / ``Med`` / ``High``), and ``repeated`` (integer repair count).
    - **Flow measurements**: raw time-series flow data for each of the six monitored areas (``Area_1.csv`` - ``Area_6.csv``) with columns ``result_time`` and ``Flow``.

    Data is loaded directly from the GitHub repository without
    requiring a local ZIP archive.

    See https://github.com/KIOS-Research/Leakage-Repairs-Dataset for details. 
    """

    #***********************************************************
    # The main method
    #***********************************************************
    def load_data(self, download_dir: str = None, areas: list[str] = None, verbose: bool = True) -> dict:
        """
        Parameters
        ----------
        download_dir : str, optional
            Path to the data files. If ``None``, the temporary folder is used.
            If the path does not exist, the data files are downloaded to the
            given location.

            The default is ``None``.

        areas : list[str], optional
            Subset of areas to load, e.g.
            ``["Area_1", "Area_3"]``.

            All entries must belong to
            ``["Area_1", ..., "Area_6"]``.

            If ``None``, data for all six areas is loaded.

            The default is ``None``.

        verbose : bool, optional
            If ``True``, progress messages are printed.

            The default is ``True``.

        Returns
        -------
        dict
            Dictionary with the following structure:

            .. code-block:: python

                {
                    "reports": pandas.DataFrame,
                    "flow": {
                        "Area_1": pandas.DataFrame,
                        "Area_2": pandas.DataFrame,
                        ...
                    }
                }

            ``reports`` contains the columns
            ``topic``, ``reason``, ``action``, ``area``,
            ``timestamp`` (datetime), ``severity``, and ``repeated``.

            Each DataFrame in ``flow`` contains the columns
            ``result_time`` (datetime) and ``Flow`` (float).

        Raises
        ------
        ValueError
            Raised if an unknown area name is passed in ``areas``.
        """

        download_dir = download_dir if download_dir is not None else get_temp_folder()
        create_path_if_not_exist(download_dir)

        if areas is None: 
            areas = _AREAS

        else: 
            unknown = set (areas) - set(_AREAS)
            if unknown:
                raise ValueError(
                    f"Unknown area(s): {unknown}."
                    f"Valid areas are: {_AREAS}"
                )
            
        results = {}


        #-------------------------------------
        # Leak reports
        #-------------------------------------
        if verbose:
            print("Loading leak reports...")

        reports_path = os.path.join(download_dir, "leak_reports.csv")
        download_if_necessary(reports_path, _REPORTS_URL, verbose)

        df_reports = pd.read_csv(reports_path)
        df_reports.columns = df_reports.columns.str.strip()     # avoid hidden tabs, spaces etc. 
        df_reports["timestamp"] = pd.to_datetime(df_reports["timestamp"])
        results["reports"] = df_reports

        #-------------------------------------
        # Flow data per area 
        #-------------------------------------

        flow_dir = os.path.join(download_dir, "raw_flow_data")
        create_path_if_not_exist(flow_dir)

        results["flow"] = {}

        for area in areas:
            if verbose:
                print(f"Loading flow data for {area}...")
            
            flow_path = os.path.join(flow_dir, f"{area}.csv")
            download_if_necessary(flow_path, _FLOW_URLS[area], verbose)

            df_flow = pd.read_csv(flow_path)
            df_flow.columns = df_flow.columns.str.strip()
            df_flow["result_time"] = pd.to_datetime(df_flow["result_time"])
            results["flow"][area] = df_flow

        if verbose:
            print("Done loading Leakage-Repairs-Dataset.")

        return results
    
register("KIOS-LeakageRepairs", LeakageRepairs)

                




    

