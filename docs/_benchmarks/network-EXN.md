---
title: "EXNET"
id: "network-exn"
permalink: /benchmarks/network-EXN.html
collection: benchmarks
layout: benchmark
---

## Description

This benchmark water system has been set up by the Centre for Water Systems of Exeter University as a realistic challenging problem. The aim is to determine the most economically effective design to reinforce the existing system to meet projected demands as a network. The network serves a population of approximately 400,000. It consists of relatively small pipes and few transmission mains, with a large head-loss range at the extremities of the system, making it highly sensitive to demand increases.

The network consists of 1893 nodes, 3029 pipes, 2 reservoirs and 2 valves.


<img src="../static/benchmarks/network-exn/exn_plot.png"/>

## How to Use

The EXN network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The EXN network is also available in Python through the key "*Network-EXN*":
```python
network = load("Network-EXN")
exn_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.EXN.load).


## Reference
Farmani, R., Savic, D. A., & Walters, G. A. (2004). *Exnet benchmark problem for multi-objective optimization of large water systems.* Modelling and control for participatory planning and managing water systems.
