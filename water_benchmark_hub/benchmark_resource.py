"""
Module provides a base class for benchmark resources such as
datasets, .inp files, control environments, etc.
"""


class BenchmarkResource():
    """
    Base class for benchmark resources such as datasets, .inp files, control environments, etc.
    """
    @staticmethod
    def get_meta_info() -> dict:
        """
        Gets the meta information of this resource.

        Returns
        -------
        `dict`
            Meta info.
        """
        raise NotImplementedError()
