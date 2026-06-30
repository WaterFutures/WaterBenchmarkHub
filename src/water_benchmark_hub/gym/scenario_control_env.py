"""
Module provides a base class for control environments.
"""
from epyt_flow.gym import ScenarioControlEnv as ScenarioControlEnvEpytFlow

from ..benchmark_resource import BenchmarkResource


class ScenarioControlEnv(ScenarioControlEnvEpytFlow, BenchmarkResource):
    """
    Base class for a control environment challenge -- inherits from
    `epyt_flow.gym.ScenarioControlEnv <https://epyt-flow.readthedocs.io/en/stable/epyt_flow.gym.html#epyt_flow.gym.scenario_control_env.ScenarioControlEnv>`_.
    """
    pass
