"""
Module provides access to the Battle of Water Demand Forecasting (BWDF) benchmark.
"""
from typing import Union, Any
import os
import pandas as pd
from epyt_flow.utils import get_temp_folder, create_path_if_not_exist, download_if_necessary

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


@meta_data("bwdf")
class BWDF(BenchmarkResource):
    """
    The Battle of Water Demand Forecasting (BWDF), organized by S. Alvisi, M. Franchini,
    V. Marsili, F. Mazzoni, E. Salomons , is the 10th in the series of
    "Battle Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.
    It took place during the 3nd International Joint Conference on Water Distribution System
    Analysis (WDSA) and Computing and Control in the Water Industry (CCWI), held in Ferrara, Italy
    in July 2024.

    This module provides functions for loading the original competition data set
    :func:`~water_benchmark_hub.bwdf.bwdf.BWDF.load_data`.
    """
    @staticmethod
    def load_data(download_dir: str = None,
                  verbose: bool = True) -> Union[pd.DataFrame, Any]:
        """
        Loads and returns the original competition data.

        .. note::

            Be aware of NaNs in the data!

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `pandas.DataFrame <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_
            Original competition data.
        """
        # Download (if necessary) and load files
        download_dir = download_dir if download_dir is not None else get_temp_folder()
        download_dir = os.path.join(download_dir, "BWDF")
        create_path_if_not_exist(download_dir)

        url_inflow_data = "https://wdsa-ccwi2024.it/wp-content/uploads/2024/03/Inflow_Data_4.xlsx"
        f_in = "Inflow_Data_4.xlsx"

        f_in = os.path.join(download_dir, f_in)
        download_if_necessary(f_in, url_inflow_data, verbose)
        df_inflow = pd.read_excel(f_in)

        url_weather_data = "https://wdsa-ccwi2024.it/wp-content/uploads/2024/03/Weather_Data_4.xlsx"
        f_in = "Weather_Data_4.xlsx"
        f_in = os.path.join(download_dir, f_in)
        download_if_necessary(f_in, url_weather_data, verbose)
        df_weather = pd.read_excel(f_in)

        # Merge data frames
        df_final = df_inflow.merge(df_weather, on="Date-time CET-CEST (DD/MM/YYYY HH:mm)")

        return df_final


register("BWDF", BWDF)
