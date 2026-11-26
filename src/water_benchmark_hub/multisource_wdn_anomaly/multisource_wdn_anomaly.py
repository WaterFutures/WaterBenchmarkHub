"""
Module provides access to the multi-source urban WDN anomaly dataset.
"""
import os 
import numpy as np
import pandas as pd

from epyt_flow.utils import create_path_if_not_exist, get_temp_folder, robust_download

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


_FILE_NAME = "input_model_potenc_predXfault7_A.csv"
_DATA_URL = f"https://zenodo.org/records/15096167/files/{_FILE_NAME}?download=1"

_TIME_COLUMN = "timestamp"
_LABEL_COLUMN = "fault_d7"

@meta_data("multisource-wdn-anomaly")
class MultiSourceWDNAnomaly(BenchmarkResource):
    """
    "Hourly Anomaly Scores and Leak Labels from a Multi-Source Urban Water 
    Distribution Network Dataset" by Babela, Munk, Munkova (2025).

    The data are hourly time series from an anonymized urban WDN combining 
    SCADA sensor readings, pumping-station energy usage, and environmental 
    conditions. Anomaly scores (0-100) were generated with Elastic ML and 
    Isolation Forest. The binary label ``fault_d7``marks hours within
    +/- 7 days of a real leak event. 

    For more information see: https://zenodo.org/records/15096167 and 
    https://www.nature.com/articles/s41597-026-07203-5

    This class provides :func:`load_data` for loading the full dataset. 
    """

    #***********************************************************
    # The main method
    #***********************************************************

    def load_data(self, download_dir:str = None, return_X_y: bool = False, 
                  verbose: bool = True)-> pd.DataFrame | tuple[np.ndarray, np.ndarray]:
        """
        Loads the full dataset. 

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.

        return_X_y : `bool`, optional
            If True, each split is returned as a ``(X, y)`` tuple of NumPy arrays,
            where ``X`` holds all anomaly-score columns and ``y`` 
            the binary ``fault_d7`` label. Otherwise, the data is returned as Pandas 
            data frame.

            The default is False.

        verbose : `bool`, optional
            If True, progress messages are printed.

            The default is True.

        Returns
        -------
        `pandas.DataFrame` or `tuple[numpy.ndarray, numpy.ndarray]`
            The full table, or ``(X, y)`` if ``return_X_y=True``.
        """

        download_dir = download_dir if download_dir is not None else get_temp_folder()
        create_path_if_not_exist(download_dir)

        f_in = os.path.join(download_dir, _FILE_NAME)
        robust_download(f_in, _DATA_URL, verbose)

        df = pd.read_csv(f_in)
        df.columns = df.columns.str.strip()
        df[_TIME_COLUMN] = pd.to_datetime(df[_TIME_COLUMN], format="%d-%m-%Y %H:%M")

        if return_X_y is True:
            feature_cols = [c for c in df.columns if c not in (_TIME_COLUMN, _LABEL_COLUMN)]
            X = df[feature_cols].to_numpy(dtype=float)
            y = df[_LABEL_COLUMN].to_numpy(dtype=int)

            return X, y

        return df

register("MultiSourceWDNAnomaly", MultiSourceWDNAnomaly)


