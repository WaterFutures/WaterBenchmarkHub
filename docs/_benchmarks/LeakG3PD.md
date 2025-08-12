---
title: "LeakG3PD: A Python Generator and Simulated Water Distribution System Dataset"
id: "leakg3pd"
permalink: /benchmarks/LeakG3PD.html
collection: benchmarks
layout: benchmark
---


## Description

LeakG3PD constitutes an updated and extended version of [LeakDB](KIOS-LeakDB.html).
The main differences are the following:
- Leak data consistency: Leak demands track pressure values according to the [WNTR](https://github.com/USEPA/WNTR) leak model equation.
- In addition to [Hanoi](network-Hanoi.html) and [Net1](network-Net1.html), [Net3](network-Net3.html) is also included.
- More realistic representations of possible leak locations: Leaks are represented as new nodes inserted within random points along random pipes.
- More variability of physical values during time: Demand patterns for different nodes are time shifted of up to 2h with 30min intervals; demand patterns have value 0 at random times.
- Improved storage features: Files for different nodes and links are grouped into single archives according to physical variables; the only scenario without any leak during the entire simulation time is scenario 0.

## How to Use

Different from the original [LeakDB](KIOS-LeakDB.html), the benchmark contains only 500 scenarios
for each network.
For each scenario, the pressure, demands, and flow rates at every node/link in the
network are provided as .csv files. The leakage location and type (abrupt, incipient) are provided
as well (see ```Leaks``` folder) -- note that not every scenario contains leakages.
Furthermore, the .inp file used for the simulation is available as well.
Labels for each time step (30-minute steps) indicating the presence of a leak
are given in ```Labels.csv```.

### Usage in Python

This benchmark is also available in Python under the key "*LeakG3PD*":
```python
leakg3pd = load("LeakG3PD")
```

Detailed information about the provided functionality can be found in the
[documentation](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.leakg3pd.html#module-water_benchmark_hub.leakg3pd.leakg3pd).

#### Loading the original data set

The original data set can be loaded as Numpy arrays by calling the
[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.leakg3pd.html#water_benchmark_hub.leakg3pd.leakg3pd.LeakG3PD.load_data)
function:
```python
# Load original data set for Net1 as labeled Numpy array
# Labels:
#   1: Leak is present
#   0: No leak is present
X, y_leak = leakg3pd.load_data(network='net1', return_X_y=True)
```

Besides loading the entire data set of 500 scenarios per network, it is also possible to load a sub-set
of scenarios only:
```python
# Load the first 10 Net1 scenarios as labeled Numpy array
X, y_leak = leakg3pd.load_data(scenarios_id=range(10), network='net1', return_X_y=True)
```
The other networks can be called by using the network parameters net3 or hanoi.

#### Loading the scenario configurations

Besides loading the original (already simulated) data sets, it is also possible to load the
scenario configuration in [EPyT-Flow](https://github.com/WaterFutures/EPyT-Flow) by calling
the [```load_scenarios()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.leakg3pd.html#water_benchmark_hub.leakg3pd.leakg3pd.LeakG3PD.load_scenarios)
function -- i.e. the user can modify the scenarios and run the simulation themself:
```python
# Load the first Net1 scenarios as an EPyT-Flow scenario
scenario, = leakg3pd.load_scenarios(scenarios_id=[0], network='net1')

# Modify scenario and run simulation
from epyt_flow.simulation import ScenarioSimulator
with ScenarioSimulator(scenario_config=scenario) as scenario:
    # ....
```
Note that due to uncertainties and other factors in the original simulation, the simulated
results will differ from the original data set and differ between runs.

## Reference

Pilotto Figueiredo, M., de Souza Oliveira, L., Lucca, G., Correa Yamin, A.,
Huckembeck dos Santos, W., da Rosa Lopes, T. (2025).
*LeakG3PD: A Python Generator and Simulated Water Distribution System Dataset.*
In: Julian, V., et al. Intelligent Data Engineering and Automated Learning -- IDEAL 2024
[<i class="bi bi-link"></i>](https://doi.org/10.1007/978-3-031-77738-7_7)