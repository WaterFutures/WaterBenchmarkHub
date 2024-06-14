---
title: "C-Town"
id: "network-ctown"
permalink: /benchmarks/network-CTown.html
collection: benchmarks
layout: benchmark
---


## Description

The C-Town network is a fictious network introduced in the [BATADAL competition](BATADAL.html).

The network consists of 388 nodes (junctions), 444 pipes, 1 reservoir, 7 tanks, 11 pumps, and 4 valves.

<img src="../static/benchmarks/network-ctown/ctown_plot.png"/>

## How to Use

C-Town is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

C-Town is also available in Python in the
[`WaterDistributionNetworks`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.WaterDistributionNetworks)
class -- can be loaded by using the key "*WaterDistributionNetworks*":
```python
networks = load("WaterDistributionNetworks")
```

Detailed information about the provided functionality can be found in the documentation of
[`load_ctown()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.WaterDistributionNetworks.load_ctown).


## Reference

Taormina, R., Galelli, S., Tippenhauer, N. O., Salomons, E., Ostfeld, A., Eliades, D. G., ... &
Ohar, Z. (2018).
*Battle of the attack detection algorithms: Disclosing cyber attacks on water distribution networks.*
Journal of Water Resources Planning and Management, 144(8), 04018048.