---
title: "LeakDB (Leakage Diagnosis Benchmark)"
id: "kios-leakdb"
permalink: /benchmarks/KIOS-LeakDB.html
collection: benchmarks
layout: benchmark
---


## Description

The increase of streaming data from water utilities is enabling the development of real-time anomaly and fault detection algorithms that can detect events, such as pipe bursts and leakages. Currently, there is not a widely accessible dataset of real or realistic leakage scenarios, which could be used as a common benchmark to compare different algorithms, as well as to support research reproducibility. In this work, we propose the design of a realistic leakage dataset, the Leakage Diagnosis Benchmark (LeakDB). The dataset is comprised of a large number of artificially created but realistic leakage scenarios, on different water distribution networks, under varying conditions. Additionally, a scoring algorithm was developed in MATLAB to evaluate the results of different algorithms using various metrics. The usage of the LeakDB dataset is demonstrated by scoring four detection algorithms. The dataset is stored in an open research data repository and will be updated in the future with new simulation scenarios. The source code of the toolkit that generates the leakage benchmark dataset, as well as the detection algorithms used, are released as open source.

## How to Use

The benchmark contains 1000 scenarios for Net1 and Hanoi network. For each scenario, the pressure, demands, and flow rates at every node/link in the network are provided as .csv files.
The leakage location and type (abrupt, incipient) are provided as well (see ```Leaks``` folder) -- note that not every scenario contains leakages.
Furthermore, the .inp file used for the simulation is available as well.
Labels for each time step (30-minute steps) indicating the presence of a leak are given in ```Labels.csv```.

### Usage in Python

This benchmark is also available in Python under the key "*KIOS-LeakDB*":
```python
leakdb = load("KIOS-LeakDB")
```

Detailed information about the provided functionality can be found in the [documentation](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.leakdb.html#module-water_benchmark_hub.leakdb.leakdb).

#### Loading the original data set

The original data set can be loaded as Numpy arrays by calling the [```load_data()```](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.leakdb.html#water_benchmark_hub.leakdb.leakdb.LeakDB.load_data) function:
```python
# Load original data set for Net1 as labeled Numpy array
# Labels:
#   1: Leak is present
#   0: No leak is present
X, y_leak = leakdb.load_data(use_net1=True, return_X_y=True)
```

Besides loading the entire data set of 1000 scenarios, it is also possible to load a sub-set of scenarios only:
```python
# Load the first 10 Net1 scenarios as labeled Numpy array
X, y_leak = leakdb.load_data(scenarios_id=range(10), use_net1=True, return_X_y=True)
```

Besides the data set, this benchmark also provides the original evaluation function implemented in [```compute_evaluation_score()```](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.leakdb.html#water_benchmark_hub.leakdb.leakdb.LeakDB.compute_evaluation_score).
In the context of the previous example of the first 10 Net1 scenarios, this could look like as follows:
```python
# Predict the presence of a leakage for each time step in each scenario
y_pred_labels_per_scenario = ...

# Evaluate prediction
score = compute_evaluation_score(scenarios_id=range(10), use_net1=True, y_pred_labels_per_scenario=y_pred_labels_per_scenario)
```

#### Loading the scenario configurations

Besides loading the original (already simulated) data sets, it is also possible to load the scenario configuration in [EPyT-Flow](https://github.com/WaterFutures/EPyT-Flow) by calling the [```load_scenarios()```](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.leakdb.html#water_benchmark_hub.leakdb.leakdb.LeakDB.load_scenarios) function -- i.e. the user can modify the scenarios and run the simulation themself:
```python
# Load the first Net1 scenarios as an EPyT-Flow scenario
scenario, = leakdb.load_scenarios(scenarios_id=[0], use_net1=True)

# Modify scenario and run simulation
from epyt_flow.simulation import ScenarioSimulator
with ScenarioSimulator(scenario_config=scenario) as scenario:
    # ....
```
Note that due to uncertainties and other factors in the original simulation, the simulated results will differ from the original data set.


## Reference

Vrachimis, S. G., Kyriakou, M. S., Eliades, D. G. and Polycarpou, M. M. (2018). *LeakDB: A benchmark dataset for leakage diagnosis in water distribution networks.* In Proc. of WDSA / CCWI Joint Conference (Vol. 1).