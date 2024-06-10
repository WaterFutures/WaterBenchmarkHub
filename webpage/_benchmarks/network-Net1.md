---
title: "Net1"
id: "network-net1"
permalink: /benchmarks/network-Net1.html
collection: benchmarks
layout: benchmark
---


## Description

The EPANET Example Network 1 (short `Net1`) constitutes a simple example of modeling chlorine decay.
Both bulk and wall reactions are included.

The network consists of 9 nodes (junctions), 12 pipes, 1 reservoir, 1 tank, and 1 pump.
Only base demands but no demand pattern is given.

<img src="/static/benchmarks/network-net1/net1_plot.png"/>

## How to Use

Net1 is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

Net1 is also available in Python in the [`WaterDistributionNetworks`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.WaterDistributionNetworks) class -- can be loaded by using the key "*WaterDistributionNetworks*":
```python
networks = load("WaterDistributionNetworks")
```

Detailed information about the provided functionality can be found in the documentation of
[`load_net1()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.WaterDistributionNetworks.load_net1).


## Reference

Rossman, L. A. (2000). EPANET 2: users manual.