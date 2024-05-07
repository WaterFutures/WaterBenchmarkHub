"""
Module provides functions for registering and loading benchmarks.
"""
from .benchmark_resource import BenchmarkResource


benchmarks = {}


def register(res_name: str, res: BenchmarkResource) -> None:
    """
    Registers a new benchmark under a given name.

    Parameters
    ----------
    res_name : `str`
        Name of the benchmark -- must be unique among all benchmarks.
    res : :class:`~water_benchmark_hub.benchmark_resource.BenchmarkResource`
        Benchmark.
    """
    if res_name in benchmarks:
        raise ValueError(f"Benchmark '{res_name}' already exists.")
    if not issubclass(res, BenchmarkResource):
        raise TypeError("'res' must be a subclass of " +
                        "'water_benchmark_hub.benchmark_resource.BenchmarkResource'")

    benchmarks[res_name] = res


def load(res_name: str) -> BenchmarkResource:
    """
    Loads a registered benchmark.

    Parameters
    ----------
    res_name : `str`
        Name of the benchmark.

    Returns
    -------
    :class:`~water_benchmark_hub.benchmark_resource.BenchmarkResource`
        Benchmark.
    """
    if res_name not in benchmarks:
        raise ValueError(f"Unknown benchmark '{res_name}'.")

    return benchmarks[res_name]
