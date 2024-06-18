"""
This module contains a class for querying the database.
"""
from typing import Any
import os
import json


class MetaData:
    """
    Class for querying the database ("webpage/static/database.json") and
    retrieving the meta info of each benchmark resource.
    """
    meta_data = None

    @staticmethod
    def get_meta_info(resource_id: str) -> dict:
        """
        Gets the meta information of a specific resource.

        Returns
        -------
        `dict`
            Meta info.
        """
        if MetaData.meta_data is None:
            with open(os.path.join(os.path.realpath(__file__).replace("meta_data.py", ""),
                                   "database.json"), "r", encoding="utf-8") as f_in:
                MetaData.meta_data = json.load(f_in)

        resources = MetaData.meta_data["resources"]

        resource_id = resource_id.lower()
        if resource_id not in resources:
            raise ValueError(f"Unknown resource '{resource_id}'")
        else:
            return resources[resource_id]


def meta_data(benchmark_id: str) -> Any:
    """
    Decorator for making the meta data available in the benchmark resource class.

    Parameters
    ----------
    benchmark_id : `str`
        ID of the benchmark resource.

    Returns
    -------
    `Any`
        Extended class.
    """
    def wrapper(my_class):
        @staticmethod
        def get_meta_info() -> dict:
            return MetaData.get_meta_info(benchmark_id)

        setattr(my_class, "get_meta_info", get_meta_info)

        return my_class

    return wrapper
