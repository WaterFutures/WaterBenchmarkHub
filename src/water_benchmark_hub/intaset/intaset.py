"""
Module provides access to the InTaSet benchmark dataset. 
"""
import os 
import numpy as np
import pandas as pd

from epyt_flow.utils import create_path_if_not_exist, download_if_necessary, get_temp_folder, unpack_zip_archive

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data




#***********************************************************
# Class 
#***********************************************************
@meta_data("InTaSet")
class InTaSet(BenchmarkResource): 

    """
    "InTaSet: A Benchmark Dataset for Data-Driven System Identification and Fault Detection
    in an Interconnected Water System" by 
    Putri, S. A., Villacrés, D., Raza, N., Iwakin, O., & Moazeni, F. (2025). 

    The **InTaSet** (Interconnected Tank System) Dataset is a comprehensive benchmark dataset 
    for nonlinear system  identification and sensor-fault detection, based on real-time measurements 
    from a physical interconnected quadruple-tank testbed operating in both 
    open-loop and closed-loop configurations. 

    The dataset contains two sub-datasets:

    - **InTaSet-ID**: system identification data across four testbed configurations (``"2T"``, ``"3T"``, ``"4T-M1"``, ``"4T-M2"``), each providing a training and a testing split 
    - **InTaSet-FD**: sensor-fault detection data consisting of clean (fault-free) training data and three fault scenarios (sensor fault at Tank 1, Tank 3, and Tank 1 & 3 simultaneously) 
    
    For more information see: https://zenodo.org/records/17652851 and https://ascelibrary.com/doi/10.1061/9780784486931.058 


    This class provides :func:`load_data` for loading the full dataset.  
    """

    #***********************************************************
    # Constants 
    #***********************************************************

    INTASET_URL = "https://zenodo.org/records/17652851/files/InTaSet.zip?download=1"

    _INTASET_ZIP = "InTaSet.zip"
    # inner folder ater extraction
    _INTASET_ROOT = os.path.join("InTaSet", "InTaSet")
    _FD_FOLDER = "InTaSet-FD"
    _ID_FOLDER = "InTaSet-ID"

    # FD clean file
    _FD_CLEAN_FILE = "Clean training data"

    # FD scenarios 
    _FD_SCENARIOS = ["Scenario 1", "Scenario 2", "Scenario 3"]

    # map scenario folder name --> fault locations 
    _FD_SCENARIO_FAULT_MAP = {
        "Scenario 1": "Tank 1",
        "Scenario 2": "Tank 3", 
        "Scenario 3": "Tank 1 and Tank 3",
    }

    # mapping the four ID configuration folder names 
    _ID_CONFIGS = {
        "2T": "InTaSet-ID-2T",
        "3T": "InTaSet-ID-3T",
        "4T-M1": "InTaSet-ID-4T-M1", 
        "4T-M2": "InTaSet-ID-4T-M2", 
    }



    #***********************************************************
    # Internal helpers 
    #***********************************************************

    @staticmethod
    def _read_xlsx(path: str) -> pd.DataFrame:
        """
        Reads an .xlsx file and normalise all column names: 
            - strips surrounding column whitespaces 
            - removes leading "- "
            - removes "x_" prefix (in FD scenario columns)
            - inserts a space before the digits, so "Tank1" becomes "Tank 1"
            - renames an unnamed first column to "Time" (missing in one of the files)
        """
        df = pd.read_excel(path, engine="openpyxl")
        
        df.columns = (
            df.columns
            .str.strip()
            .str.lstrip("- ")
            .str.replace(r"^x_", "", regex=True)
            .str.replace(r"(\d+)$", r" \1", regex=True)
        )
        
        if df.columns[0] in ("", "Unnamed: 0"):
            df = df.rename(columns={df.columns[0]: "Time"})
        
        return df
    
    @staticmethod
    def _find_xlsx(folder: str, keyword: str) -> str | None: 
        """
        Returns the path of the first ``.xlsx`` file in *folder* whose name 
        contains *keyword*, or ``None`` if not found.
        """
        if not os.path.exists(folder):
            return None
        for f in os.listdir(folder):
            if keyword.lower() in f.lower() and f.endswith(".xlsx"):
                return os.path.join(folder, f)
        return None
    

    @staticmethod
    def _to_X_y_fd(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray | None]:
        """
        Returns ``(X, y)`` for an FD Dataframe. 
        ``y`` is ``None`` when no ``Label`` column is present (clean data).
        """
        feature_cols = [c for c in df.columns if c not in ("Time", "Label")]
        X = df[feature_cols].to_numpy(dtype=float)
        y = df["Label"].to_numpy(dtype=int) if "Label" in df.columns else None
        
        return X, y

    @staticmethod
    def _to_X_y_id(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]: 
        """
        Returns ``(X, y)`` for an ID Dataframe. 
        ``X`` contains pump (input) columns and ``y`` contains tank-level columns (output).
        """
        pump_cols = [c for c in df.columns if "pump" in c.lower()]
        tank_cols = [c for c in df.columns if "tank" in c.lower()]
        X = df[pump_cols].to_numpy(dtype=float)
        y = df[tank_cols].to_numpy(dtype=float)

        return X, y


    #***********************************************************
    # The main method
    #***********************************************************
    def load_data(self, download_dir:str = None, return_X_y: bool = False, verbose: bool = True) -> dict:

        """
        Loads the full InTaSet benchmark dataset. 

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.

        return_X_y : `bool`, optional
            If True, each split is returned as a ``(X, y)`` tuple of NumPy arrays,
            otherwise, the data is returned as Pandas data frame.

            - **FD clean**: ``(X, None)`` - no fault labels available.
            - **FD scenarios**: ``(X, y)`` where ``y`` is the integer
              ``Label`` column (fault indicator).
            - **ID splits**: ``(X, y)`` where ``X`` are the pump input
              columns and ``y`` are the tank-level output columns.

            The default is False.

        verbose : `bool`, optional
            If True, progress messages are printed.

            The default is True.
            
        Returns
        -------
        dict
            Nested dictionary with the following structure:

            .. code-block:: python

                {
                    "ID": {
                        "2T": {"train": ..., "test": ...},
                        "3T": {"train": ..., "test": ...},
                        "4T-M1": {"train": ..., "test": ...},
                        "4T-M2": {"train": ..., "test": ...}
                    },

                    "FD": {
                        "clean": ...,       # fault-free data
                        "scenario_1": ...,  # sensor fault at Tank 1
                        "scenario_2": ...,  # sensor fault at Tank 3
                        "scenario_3": ...   # sensor fault at Tank 1 & Tank 3
                    }
                }

            Each value is either:
            
            - ``pandas.DataFrame`` if ``return_X_y=False``
            - or ``(X, y)`` NumPy tuple if ``return_X_y=True``

        """

        
        
        # Download data if necessary
        download_dir = download_dir if download_dir is not None else get_temp_folder()

        zip_path = os.path.join(download_dir, self._INTASET_ZIP)

        if self.INTASET_URL is not None: 
            download_if_necessary(zip_path, self.INTASET_URL, verbose)
        elif not os.path.exists(zip_path): 
            raise FileNotFoundError(f"{self._INTASET_ZIP}' not found in '{download_dir}'." 
                                    f"Please download InTaSet manually and place the zip file in that directory.")
        
        if verbose:
            print("Extracting InTaSet.zip ...")

        #root = os.path.join(download_dir, self._INTASET_ROOT)
        root = os.path.join(download_dir, "InTaSet")

        create_path_if_not_exist(root)
        unpack_zip_archive(zip_path, download_dir)

        results = {"ID": {}, "FD": {}}


        #-------------------------------------
        # FD 
        #-------------------------------------

        fd_root = os.path.join(root, self._FD_FOLDER)

        #------------------------------
        # FD clean training data
        #------------------------------
        fd_directory = os.path.join(fd_root, self._FD_CLEAN_FILE)

        if verbose: 
            print("Loading FD: clean training data ...")
        
        clean_path = self._find_xlsx(fd_directory, "InTaSet-FD-Training")

        if clean_path is None: 
            raise FileNotFoundError(f"Clean training data file is not found in '{fd_root}'")
        
        df_clean = self._read_xlsx(clean_path)
        results["FD"]["Clean"] = (
            self._to_X_y_fd(df_clean) if return_X_y else df_clean
        )

        for scenario_folder in self._FD_SCENARIOS: 

            key = scenario_folder.lower().replace(" ", "_")    # "scenario_1" instead of "Scenario 1"

            scenario_dir = os.path.join(fd_root, scenario_folder)

            if not os.path.exists(scenario_dir): 
                if verbose: 
                    print (f"Warning: {scenario_folder} not found! Skipping.")
                continue

            fault = self._FD_SCENARIO_FAULT_MAP.get(scenario_folder, "unknown") # unknown instead of error in case no value found for a key 

            if verbose:
                print(f"Loading FD: {scenario_folder} (sensor fault at {fault}) ...")

            xlsx_files = [f for f in os.listdir(scenario_dir) if f.endswith(".xlsx")]

            if not xlsx_files:
                raise FileNotFoundError(f"No .xlsx file found in {scenario_dir}")
            
            df = self._read_xlsx(os.path.join(scenario_dir, xlsx_files[0]))

            results["FD"][key] = (
                self._to_X_y_fd(df) if return_X_y else df
            )

        #-------------------------------------
        # ID (four configurations)
        #-------------------------------------

        id_root = os.path.join(root, self._ID_FOLDER)

        for config_key, config_folder in self._ID_CONFIGS.items():
            if verbose:
                print(f"Loading ID: {config_key} ...")
            
            config_path = os.path.join(id_root, config_folder)

            results["ID"][config_key] = {}

            for split in ("train", "test"):
                base_label = "Training" if split == "train" else "Testing"

                candidates = [
                    base_label, 
                    base_label.lower(),
                ]

                sub_folder = None
                matched_label = None
                xlsx_path = None

                for split_label in candidates:  
                    # files may sit inside a named subfolder, e.g. InTaSet-ID-4T-M1_Training
                    candidate_folder = f"{config_folder}_{split_label}"
                    sub_folder = os.path.join(config_path, candidate_folder)

                    xlsx_path = (
                        self._find_xlsx(sub_folder, split_label) or
                        self._find_xlsx(config_path, split_label)
                    )

                    if xlsx_path is not None:
                        matched_label = split_label
                        break 
                
                if xlsx_path is None:
                    raise FileNotFoundError(
                        f"Could not find Training/Testing xlsx for ID config '{config_key}' in '{config_path}'"
                    )
                
                df = self._read_xlsx(xlsx_path)
                results["ID"][config_key][split] = (
                    self._to_X_y_id(df) if return_X_y else df
                )

        if verbose:
            print ("Done loading InTaSet.")
        
        return results    
register("InTaSet", InTaSet)



                





        


                





