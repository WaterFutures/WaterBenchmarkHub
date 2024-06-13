"""
This module contains a class for querying the database.
"""
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
