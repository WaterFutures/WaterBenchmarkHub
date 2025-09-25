"""
Module provides access to the Battle of Water Demand Forecasting (BWDF) benchmark.
"""
from typing import Union, List

import pandas as pd

import wf4bwdf

from ..benchmark_resource import BenchmarkResource
from ..benchmarks import register
from ..meta_data import meta_data

@meta_data("bwdf")
class BWDF(BenchmarkResource):
    """
    The Battle of Water Demand Forecasting (BWDF), organized by S. Alvisi, M. Franchini,
    V. Marsili, F. Mazzoni, and E. Salomons, is the 10th in the series of
    "Battle of the Water Networks series" dating back to the Battle of the Water Networks (BWN) in 1985.
    It took place during the 3rd International Joint Conference on Water Distribution System
    Analysis (WDSA) and Computing and Control in the Water Industry (CCWI), held in Ferrara, Italy
    in July 2024.
    For more information, see [Alvisi et al. (2025)](https://ascelibrary.org/doi/10.1061/JWRMD5.WRENG-6887).

    This module provides functions for loading the original competition dataset, the complete
    dataset released as supplementary material to the publication, and for testing your forecasts
    using the same specifications as the original competition.

    Note:
        This module exposes only the core functionalities of the more extended package `wf4bwdf`.
        To access additional features and utilities, please install the extended package:

            pip install wf4bwdf

        For more details, visit the [wf4bwdf documentation or repository](https://github.com/WaterFutures/wf4bwdf).

    Functions:
        - :func:`~water_benchmark_hub.bwdf.bwdf.BWDF.load_complete_dataset`
        - :func:`~water_benchmark_hub.bwdf.bwdf.BWDF.load_iteration_dataset`
        - :func:`~water_benchmark_hub.bwdf.bwdf.BWDF.evaluate`
    """
    @staticmethod
    def load_complete_dataset(
        use_letters_for_names:bool=False
        ) -> dict[str, pd.DataFrame]:
        """
        Load the complete dataset containing all DMA inflows, weather data, properties, and calendar information.
        
        This function loads and returns the complete dataset released as supplementary
        information after the end of the competition. It includes including
        historical DMA inflow measurements, weather observations, DMA properties, and calendar metadata.
        The complete dataset contains both training and evaluation period data, it's 
        the user responsability to handle the dataset correctly.
        
        Parameters
        ----------
        use_letters_for_names : bool, default False
            If True, uses alphabetical names for DMAs (e.g., 'DMA A', 'DMA B', 'DMA C').
            If False, uses numerical names for DMAs (e.g., 'DMA 1', 'DMA 2').
        
        Returns
        -------
        dict[str, pd.DataFrame]
            Dictionary containing the complete dataset with the following keys:

            **'dma-properties'**: DataFrame with DMA properties and characteristics (DMA name as index):
                - "Short name": string with short name of the DMA (e.g., 'A', 'B', '3', '9')
                - "Description": string of the original documentation description of the DMAs
                - "Category": string that is a short description and can be used to tag the dmas. Use this info as a categorical
                - "Population": list of int with the population served by each DMA 
                - "Mean hourly flow (L/s/hour)": list of float with the mean hourly flow in L/s of each DMA 

            ---
            **'dma-inflows'**: DataFrame with historical inflow measurements for all DMAs

            ---
            **'weather'**: DataFrame with weather observation data

            ---
            **'calendar'**: DataFrame with calendar information:
                - 'CEST': bool indicating if daylight savings time is active,
                - 'Holiday': bool indicating if the day is a holiday or a sunday
                - 'Dataset week number': int indicating the absolute week number in the dataset, starts from 0 and week 1 starts on the 4th of January 2021
                - 'Iteration': int indicating in which original iteration of the competition this measurement was released. Goes between 1 and 4 included, 5 indicates additional measurements not available during the competition
                - 'Evaluation week': bool indicating if the measurement is part of of the original competition evaluation weeks
        
        Raises
        ------
        TypeError
            If use_letters_for_names is not a boolean value.
        
        Notes
        -----
        - This function loads the complete dataset including evaluation period data
        - To compare your approach with the battle competitors use load_iteration_dataset() to get filtered data up to a specific iteration
        
        Examples
        --------
        >>> # Load complete dataset with numerical DMA names
        >>> dataset = load_complete_dataset()
        >>> print(dataset.keys())
        dict_keys(['dma-properties', 'dma-inflows', 'weather', 'calendar'])
        
        >>> # Load complete dataset with alphabetical DMA names
        >>> dataset = load_complete_dataset(use_letters_for_names=True)
        >>> print(dataset['dma-inflows'].columns[:3])  # First 3 DMA columns
        Index(['DMA A', 'DMA B', 'DMA C'], dtype='object')
        """
        return wf4bwdf.load_complete_dataset(use_letters_for_names=use_letters_for_names)
    
    @staticmethod
    def load_iteration_dataset(
        iteration: int,
        use_letters_for_names:bool=False,
        keep_evaluation_week: bool=False
    ) -> dict[str, pd.DataFrame]:
        """
        Load dataset as it was made available during the competition until the requested
        iteration.
        
        This function include only data available up to the specified iteration as if
        you were participating again in the competition.
        
        Parameters
        ----------
        iteration : int
            The iteration number to filter data up to. Must be between 1 and 4 inclusive.
        use_letters_for_names : bool, default False
            If True, uses alphabetical names for DMAs (e.g., 'DMA A', 'DMA B', 'DMA C').
            If False, uses numerical names for DMAs (e.g., 'DMA 1', 'DMA 2').
        keep_evaluation_week: bool, default False
            If True, the week to forecast appears in the 'dma-inflow' DataFrame but all the values are NaN.
            If False, the 'dma-inflow' DataFrame is one week shorter than the calendar and the weather DataFrames. 

        Returns
        -------
        dict[str, pd.DataFrame]
            Dictionary containing the complete dataset with the following keys:

            **'dma-properties'**: DataFrame with DMA properties and characteristics (DMA name as index):
                - "Short name": string with short name of the DMA (e.g., 'A', 'B', '3', '9')
                - "Description": string of the original documentation description of the DMAs
                - "Category": string that is a short description and can be used to tag the dmas. Use this info as a categorical
                - "Population": list of int with the population served by each DMA 
                - "Mean hourly flow (L/s/hour)": list of float with the mean hourly flow in L/s of each DMA
            
            ---
            **'dma-inflows'**: DataFrame with historical inflow measurements for all DMAs
            
            ---
            **'weather'**: DataFrame with weather observation data
            
            ---
            **'calendar'**: DataFrame with calendar information:
                - 'CEST': bool indicating if daylight savings time is active,
                - 'Holiday': bool indicating if the day is a holiday or a sunday
                - 'Dataset week number': int indicating the absolute week number in the dataset, starts from 0 and week 1 starts on the 4th of January 2021
                - 'Iteration': int indicating in which original iteration of the competition this measurement was released. Goes between 1 and 4 included, 5 indicates additional measurements not available during the competition
                - 'Evaluation week': bool indicating if the measurement is part of of the original competition evaluation weeks
        
        Raises
        ------
        ValueError
            If iteration is not an integer or is outside the valid range [1, 4].
        TypeError
            If use_letters_for_names or keep_evaluation_week are not a boolean value.
        
        Notes
        -----
        - This function is designed to put the user in the same situation as the competitors were and simulate the same procedure
        
        Examples
        --------
        >>> # Load data up to iteration 3
        >>> dataset = load_iteration_dataset(iteration=3)
        >>> # Check that evaluation week data is masked
        >>> eval_mask = dataset['calendar']['Evaluation week']
        >>> print(dataset['dma-inflows'].loc[eval_mask].isna().all().all())
        True
        
        >>> # Load data for first iteration with alphabetical names
        >>> dataset = load_iteration_dataset(iteration=1, use_letters_for_names=True)
        >>> print(f"Data available until iteration: {dataset['calendar']['Iteration'].max()}")
        Data available until iteration: 1
        """
        return wf4bwdf.load_iteration_dataset(
            iteration=iteration,
            use_letters_for_names=use_letters_for_names,
            keep_evaluation_week=keep_evaluation_week
        )

    @staticmethod
    def evaluate(forecast: Union[pd.DataFrame, pd.Series, List[pd.Series]]) -> pd.Series:
        """
        Evaluate forecast performance against ground truth data using the Battle of 
        the Water Demand Forecasting original evalutation weeks and performance indicators.
        
        This function computes three performance indicators (PI1, PI2, PI3) for each DMA (District 
        Metered Area) across different evaluation weeks by comparing forecast values against actual 
        inflow measurements. It infers automatially the evaluation week and DMA to test
        based on the input. 
        
        Parameters
        ----------
        forecast : Union[pd.DataFrame, pd.Series, List[pd.Series]]
            Forecast data to evaluate. Can be:
            - DataFrame with DMAs as columns and dates as index
            - Series with forecast values for a single DMA
            - List of Series, each representing forecasts for different DMAs
            The index should contain dates that correspond to the original evaluation weeks.
            DMA names can be either numerical or alphabetical format and only the existing ones 
            are evaluated.
        
        Returns
        -------
        pd.Series
            A MultiIndex Series with performance indicator values. The index has three levels:
            - Level 0: 'Evaluation week' name [W1, W2, W3, W4] deduced by the forecast dates
            - Level 1: DMA identifier (numerical or alphabetical name)
            - Level 2: Performance indicator name ('PI1', 'PI2', 'PI3')
            
            The Series values are the computed performance indicator scores for each 
            (evaluation_week, dma, pi) combination.
        
        Notes
        -----
        - Loads ground truth data automatically
        - Handles both numerical and alphabetical DMA naming conventions
        - Computes three performance indicators (PI1, PI2, PI3) for comprehensive evaluation
        - Deduces automatically the evaluation week and DMA(s) to test.
        
        Examples
        --------
        >>> # Evaluate a DataFrame forecast
        >>> forecast_df = pd.DataFrame(...)  # forecast data
        >>> results = evaluate(forecast_df)
        >>> print(results.loc[('W1', 'DMA 1', 'PI1')])  # Access specific result
        
        >>> # Evaluate a single DMA forecast
        >>> forecast_series = pd.Series(...)  # single DMA forecast
        >>> results = evaluate(forecast_series)
        >>> print(results.loc[('W1', 'DMA C', 'PI1')])  # Still need to access as a multi-index
        """
        return wf4bwdf.evaluate(forecast=forecast)

register("BWDF", BWDF)
