"""
Module provides access to the WDSEventDB benchmark dataset. 
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
@meta_data("WDSEventDB")
class WDSEventDB(BenchmarkResource):
    """
    "WDSEventDB: A Real-Time Benchmark Dataset for Event Diagnosis in 
    Water Distribution Networks" by 
    Raza, N., Iwakin, O., Daniela, V., Putri, S. A., & Moazeni, F. (2025). 
   
    The **WDSEventDB** (Water Distribution System Event Database) benchmark is an open-source, 
    real-time dataset collected from a sensor-instrumented water distribution testbed, 
    featuring cyberattack, leakage, and sensor-failure events for event diagnosis and anomaly detection research.

    It contains measurements collected from a physical WDS testbed under four operating conditions: 

    - **Clean** — fault-free baseline data (``CleanData.xlsx``).
    - **Cyberattack** — one combined cyber-event file covering events 1-4 (``CyberEvent1-4.xlsx``).
    - **Leakage** — three individual leakage event files(``LeakEvent1 - 3.xlsx``).
    - **Sensor Failure** — four sensor-failure event files covering sensor pairs 1, 2-3, 4-5, and 6-7 (``SensorEvent1.xlsx``, ``SensorEvent23.xlsx``, ``SensorEvent45.xlsx``, ``SensorEvent67.xlsx``).

    Every fole shares the same 16-column strucure: four pressure sensors, four flow meters, four VFD actuators 
    (one split into two channels), two analogue valves, and a ``Labels`` column.

    For more information see: https://zenodo.org/records/17547955 and https://ascelibrary.com/doi/abs/10.1061/9780784486931.069

    This class provides :func:`load_data` for loading the full dataset.  
    
    """



    #***********************************************************
    # Constants 
    #***********************************************************

    WDSEventDB_URL = "https://zenodo.org/records/17547955/files/WDSEventDB.zip?download=1"

    _WDS_EVENT_ZIP = "WDSEventDB.zip"
    _WDSEVENT_ROOT = os.path.join("WDSEventDB", "WDSEvenDB")

    _FOLDER_CLEAN = "Clean"
    _FOLDER_CYBERATTACK = "Cyberattack"
    _FOLDER_LEAKAGE = "Leakage"
    _FOLDER_SENSOR_FAILURE = "Sensor Failure"

    # features = all columns, but no Labels
    _FEATURE_COLUMNS = [
        "Pressure 1 Out", "Pressure 2 Out", "Pressure 3 In", "Pressure 4 In",
        "Water Flow 1",   "Water Flow 2",   "Water Flow 3",  "Water Flow 4",
        "VFD 1", "VFD 2", "VFD 3", "VFD 4-1", "VFD 4-2",
        "Analog Valve 1", "Analog Valve 2",
    ]

    _LABEL_COLUMN = "Labels"



    #***********************************************************
    # Internal helpers 
    #***********************************************************

    @staticmethod
    def _read_xlsx(path: str) -> pd.DataFrame:
        """
        Reads an .xlsx file and strips surrounding whitespace from column names. 
        """
        df = pd.read_excel(path, engine="openpyxl")
        df.columns = df.columns.str.strip()
        return df 
    
    @staticmethod
    def _load_folder(folder_path: str, filenames: list[str], return_X_y: bool) -> dict | tuple: 
        """
        Loads one or more .xlsx files from a folder.          
        """

        results = {}
        for filename in filenames: 
            path = os.path.join(folder_path, filename)
            df = WDSEventDB._read_xlsx(path)
            # strips .xlsx
            key = os.path.splitext(filename)[0]  

            if return_X_y: 
                X = df[WDSEventDB._FEATURE_COLUMNS].to_numpy(dtype=float)
                y = (df[WDSEventDB._LABEL_COLUMN].to_numpy(dtype=int) if WDSEventDB._LABEL_COLUMN in df.columns else None)
                results[key] = (X, y)
            else: 
                results[key] = df

        return results
    


    #***********************************************************
    # The main method
    #***********************************************************
    def load_data(self, download_dir:str = None, return_X_y: bool = False, verbose: bool = True) -> dict:
        """
        Loads the full WDSEventDB benchmark dataset. 

        Parameters
        ----------
        download_dir : `str`, optional
            Path to the data files -- if None, the temp folder will be used.
            If the path does not exist, the data files will be downloaded to the given path.

            The default is None.

        return_X_y : `bool`, optional
            If True, each entry is returned as a ``(X, y)`` tuple of NumPy arrays where ``X`` 
            contains the , 15 sensor/actuator feature columns and ``y`` contains the integer ``Labels`` column. 
            Otherwise, the data is returned as Pandas data frame.

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
                    "clean": {
                        "CleanData": ...,          # fault-free baseline data
                    },

                    "cyberattack": {
                        "CyberEvent1-4": ...,      # combined cyberattack scenarios
                    },

                    "leakage": {
                        "LeakEvent1": ...,         # leakage scenario 1
                        "LeakEvent2": ...,         # leakage scenario 2
                        "LeakEvent3": ...,         # leakage scenario 3
                    },

                    "sensor_failure": {
                        "SensorEvent1": ...,       # sensor failure at location 1
                        "SensorEvent23": ...,      # sensor failures at sensors 2 & 3
                        "SensorEvent45": ...,      # sensor failures at sensors 4 & 5
                        "SensorEvent67": ...,      # sensor failures at sensors 6 & 7
                    }
                }

            Each value is either:

            - ``pandas.DataFrame`` if ``return_X_y=False``
            - or ``(X, y)`` NumPy tuple if ``return_X_y=True``


        """

        download_dir = download_dir if download_dir is not None else get_temp_folder()

        zip_path = os.path.join(download_dir, self._WDS_EVENT_ZIP)

        if self.WDSEventDB_URL is not None:
            download_if_necessary(zip_path, self.WDSEventDB_URL, verbose)
        elif not os.path.exists(zip_path): 
            raise FileNotFoundError(f"{self._WDS_EVENT_ZIP}' not found in '{download_dir}'." 
                                    f"Please download WDSEventDB manually and place the zip file in that directory.")
        
        if verbose:
            print("Extracting WDSEventDB.zip ...")
        
        #root = os.path.join(download_dir, self._WDSEVENT_ROOT)
        root = os.path.join(download_dir, "WDSEventDB")
        create_path_if_not_exist(root)
        unpack_zip_archive(zip_path, download_dir)

        results = {}

        #-------------------------------------
        # Clean 
        #-------------------------------------

        if verbose:
            print("Loading Clean data ...")
        
        results["clean"] = self._load_folder(
            folder_path=os.path.join(root, self._FOLDER_CLEAN),
            filenames=["CleanData.xlsx"],
            return_X_y=return_X_y,
        )

        #-------------------------------------
        # Cyberattack 
        #-------------------------------------
        if verbose:
            print("Loading Cyberattack data ...")

        results["cyberattack"] = self._load_folder(
            folder_path=os.path.join(root, self._FOLDER_CYBERATTACK),
            filenames=["CyberEvent1-4.xlsx"],
            return_X_y=return_X_y,
        )

        #-------------------------------------
        # Leakage
        #-------------------------------------
        if verbose:
            print("Loading Leakage data ...")

        results["leakage"] = self._load_folder(
            folder_path=os.path.join(root, self._FOLDER_LEAKAGE),
            filenames=["LeakEvent1.xlsx", "LeakEvent2.xlsx", "LeakEvent3.xlsx"],
            return_X_y=return_X_y,
        )

        #-------------------------------------
        # Sensor Failure
        #-------------------------------------
        if verbose:
            print("Loading Sensor Failure data ...")

        results["sensor_failure"] = self._load_folder(
            folder_path=os.path.join(root, self._FOLDER_SENSOR_FAILURE),
            filenames=["SensorEvent1.xlsx", "SensorEvent23.xlsx", "SensorEvent45.xlsx", "SensorEvent67.xlsx"],
            return_X_y=return_X_y,
        )

        if return_X_y: 
            # collect all (X, y) pairs from every file across all categories
            all_X, all_y = [], []
            for category in ["clean", "cyberattack", "leakage", "sensor_failure"]:
                # cat_data is a dict of (X, y) tuples
                cat_data = results[category]
                for key, (X, y) in cat_data.items():
                    all_X.append(X)
                    if y is not None:
                        all_y.append(y)
                    else:
                        # clean should not have any labels, so fill with 0 (already in the files)
                        all_y.append(np.zeros(len(X), dtype=int))
            return np.concatenate(all_X, axis=0), np.concatenate(all_y, axis=0)


        if verbose:
            print("Done loading WDSEventDB.")

        return results   
register("WDSEventDB", WDSEventDB)
