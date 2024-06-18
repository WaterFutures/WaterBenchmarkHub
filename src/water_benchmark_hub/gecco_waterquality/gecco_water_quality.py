"""
Module provides functions for loading different GECCO water quality data sets.
"""
import os
from typing import Union
import numpy as np
import pandas as pd
from epyt_flow.utils import get_temp_folder, download_if_necessary

from ..metrics import f1_score
from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data


class GeccoWaterQuality(BenchmarkResource):
    """
    Base class for GECCO Water Quality 2017 - 2019 benchmarks.

    Note that the scoring/evaluation algorithm is the same for all GECCO water quality benchmarks
    and is implemented in
    :func:`~water_benchmark_hub.gecco_waterquality.gecco_water_quality.GeccoWaterQuality.compute_evaluation_score`.
    """
    @staticmethod
    def get_meta_info() -> dict:
        raise NotImplementedError()

    @staticmethod
    def compute_evaluation_score(y_pred: np.ndarray, y: np.ndarray) -> float:
        """
        Evaluates the performance of a detection method.

        .. note::
            All GECCO water quality challenges use the F1-score for evaluation.

        Parameters
        ----------
        y_pred : `numpy.ndarray`
            Event indication prediction over time
        y : `numpy.ndarray`
            Ground truth event indication over time.

        Returns
        -------
        `float`
            Evaluation score.
        """
        return f1_score(y_pred, y)


@meta_data("gecco-waterquality2017")
class GeccoWaterQuality2017(GeccoWaterQuality):
    """
    Class for Loading the original GECCO Industrial Challenge 2017 Dataset: A water quality dataset for the
    "Monitoring of drinking-water quality" competition organized by M. Friese, J. Stork,
    A. Fischbach, M. Rebolledo, T. Bartz-Beielstein at the Genetic and Evolutionary
    Computation Conference 2017, Berlin, Germany

    This is a benchmark for anomaly detection algorithms on water quality. The data is provided by
    the "Thüringer Fernwasserversorgung" (Germany) and constitutes a real-world data set. In this
    data set, 9 numeric water quality features are given at a sampling rate of 1 min over approx.
    3 month. The goal is to predict the presence of an anomaly -- i.e. binary classification.

    More information can be found at https://zenodo.org/records/3884465 and
    http://www.spotseven.de/gecco-challenge/gecco-challenge-2017/
    """
    @staticmethod
    def load_data(download_dir: str = None, return_X_y: bool = True, verbose: bool = True
                  ) -> Union[pd.DataFrame, tuple[np.ndarray, np.ndarray]]:
        """
        Loads the original GECCO Industrial Challenge 2017 Dataset.

        .. note::

            Note that this is NOT a simulated scenario and therefore only the final
            data set is provided.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        return_X_y : `bool`, optional
            If True, the data is returned together with the labels as two Numpy arrays,
            otherwise the data is returned as Pandas data frame.

            The default is True.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `pandas.DataFrame` or `tuple[numpy.ndarray, numpy.ndarray]`
            The benchmark data set as either a Pandas data frame or as a pair of (X, y) Numpy arrays.
        """
        url_data = "https://zenodo.org/records/3884465/files/1_gecco2017_water_quality.csv?download=1"

        download_dir = download_dir if download_dir is not None else get_temp_folder()
        f_in = os.path.join(download_dir, "gecco2017_water_quality.csv")

        download_if_necessary(f_in, url_data, verbose)

        # Load and return data
        df_data = pd.read_csv(f_in, index_col=0)

        if return_X_y is False:
            return df_data
        else:
            y = df_data["EVENT"].to_numpy().astype(np.int8)
            del df_data["EVENT"]

            del df_data["Time"]
            X = df_data.to_numpy()

            return X, y


@meta_data("gecco-waterquality2018")
class GeccoWaterQuality2018(GeccoWaterQuality):
    """
    Class for Loading the GECCO Industrial Challenge 2018 Dataset: A water quality dataset for the
    "Internet of Things: Online Anomaly Detection for Drinking Water Quality" competition
    organized by F. Rehbach, M. Rebolledo, S. Moritz, S. Chandrasekaran, T. Bartz-Beielstein at
    the Genetic and Evolutionary Computation Conference 2018, Kyoto, Japan.

    This is a benchmark (based on
    :func:`~~water_benchmark_hub.gecco_water_quality.GeccoWaterQuality2017`)
    for anomaly detection algorithms on water quality. The data is provided by the
    "Thüringer Fernwasserversorgung" (Germany) and constitutes a real-world data set. In this
    data set, 9 numeric water quality features are given at a sampling rate of
    1 min over approx. 3 month. The goal is to predict the presence of an anomaly -- i.e.
    binary classification.

    More information can be found at https://zenodo.org/records/3884398 and
    http://www.spotseven.de/gecco/gecco-challenge/gecco-challenge-2018/
    """
    @staticmethod
    def load_data(download_dir: str = None, return_X_y: bool = True, verbose: bool = True
                  ) -> Union[pd.DataFrame, tuple[np.ndarray, np.ndarray]]:
        """
        Loads the GECCO Industrial Challenge 2018 Dataset.

        .. note::

            Note that this is NOT a simulated scenario and therefore only the final
            data set is provided.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        return_X_y : `bool`, optional
            If True, the data is returned together with the labels as two Numpy arrays,
            otherwise the data is returned as Pandas data frame.

            The default is True.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `pandas.DataFrame` or `tuple[numpy.ndarray, numpy.ndarray]`
            The benchmark data set as either a Pandas data frame or
            as a pair of (X, y) Numpy arrays.
        """
        # Download data if necessary
        url_data = "https://zenodo.org/records/3884398/files/1_gecco2018_water_quality.csv?download=1"

        download_dir = download_dir if download_dir is not None else get_temp_folder()
        f_in = os.path.join(download_dir, "gecco2018_water_quality.csv")

        download_if_necessary(f_in, url_data, verbose)

        # Load and return data
        df_data = pd.read_csv(f_in, index_col=0)

        if return_X_y is False:
            return df_data
        else:
            y = df_data["EVENT"].to_numpy().astype(np.int8)
            del df_data["EVENT"]

            del df_data["Time"]
            X = df_data.to_numpy()

            return X, y


@meta_data("gecco-waterquality2019")
class GeccoWaterQuality2019(GeccoWaterQuality):
    """
    Class for Loading GECCO Industrial Challenge 2019 Dataset: A water quality dataset for the
    "Internet of Things: Online Event Detection for Drinking Water Quality Control" competition
    organized by F. Rehbach, S. Moritz, T. Bartz-Beielstein at the Genetic and
    Evolutionary Computation Conference 2019, Prague, Czech Republic.

    This is a benchmark (based on
    :class:`~water_benchmark_hub.gecco_water_quality.GeccoWaterQuality2018`)
    for anomaly detection algorithms on water quality. The data is provided by the
    "Thüringer Fernwasserversorgung" (Germany) and constitutes a real-world data set. In this
    data set, 6 numeric water quality features are given at a sampling rate of 1 min over approx.
    3 month. The goal is to predict the presence of an anomaly -- i.e. binary classification.
    The data set itself comes in three splits: A train set, a validation set, and a test set.

    More information can be found at https://zenodo.org/records/4304080 and
    https://www.th-koeln.de/informatik-und-ingenieurwissenschaften/gecco-challenge-2019_63244.php
    """
    @staticmethod
    def load_data(download_dir: str = None, return_X_y: bool = True, verbose: bool = True) -> dict:
        """
        Loads GECCO Industrial Challenge 2019 Dataset.

        .. note::

            Note that this is NOT a simulated scenario and therefore only the final
            data set is provided.

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.
        return_X_y : `bool`, optional
            If True, the data is returned together with the labels as two Numpy arrays,
            otherwise the data is returned as Pandas data frame.

            The default is True.
        verbose : `bool`, optional
            If True, a progress bar is shown while downloading files.

            The default is True.

        Returns
        -------
        `dict`
            The data set as a dictionary with entries "train", "validation", and "test" containing
            the respective data.
        """
        # Download data if necessary
        download_dir = download_dir if download_dir is not None else get_temp_folder()

        base_url = "https://zenodo.org/records/4304080/files/"
        url_train_data = base_url + "7_gecco2019_train_water_quality.csv?download=1"
        url_valid_data = base_url + "8_gecco2019_valid_water_qulity.csv?download=1"
        url_test_data = base_url + "6_gecco2019_test_water_quality.csv?download=1"

        f_train_in = os.path.join(download_dir, "gecco2019_train_water_quality.csv")
        f_valid_in = os.path.join(download_dir, "gecco2019_valid_water_qulity.csv")
        f_test_in = os.path.join(download_dir, "gecco2019_test_water_quality.csv")

        download_if_necessary(f_train_in, url_train_data, verbose)
        download_if_necessary(f_valid_in, url_valid_data, verbose)
        download_if_necessary(f_test_in, url_test_data, verbose)

        # Load and return data
        df_data_train = pd.read_csv(f_train_in, index_col=0)
        df_data_valid = pd.read_csv(f_valid_in, index_col=0)
        df_data_test = pd.read_csv(f_test_in, index_col=0)

        if return_X_y is False:
            return {"train": df_data_train, "validation": df_data_valid, "test": df_data_test}
        else:
            r = {"train": None, "validation": None, "test": None}

            for k, df_data in zip(["train", "validation", "test"],
                                  [df_data_train, df_data_valid, df_data_test]):
                y = df_data["Event"].to_numpy().astype(np.int8)
                del df_data["Event"]

                del df_data["Time"]
                X = df_data.to_numpy()

                r[k] = (X, y)

            return r


register("GECCO-WaterQuality2017", GeccoWaterQuality2017)
register("GECCO-WaterQuality2018", GeccoWaterQuality2018)
register("GECCO-WaterQuality2019", GeccoWaterQuality2019)
