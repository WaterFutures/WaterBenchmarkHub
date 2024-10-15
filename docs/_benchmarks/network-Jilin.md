---
title: "Jilin"
id: "network-jilin"
permalink: /benchmarks/network-Jilin.html
collection: benchmarks
layout: benchmark
---


## Description

The Jilin network was designed to research pipe size optimization and chlorine distribution in WDN.

The network consists of 27 junctions, 34 pipes and 1 reservoir. It contains a demand pattern for 4 days.

<img src="../static/benchmarks/network-jilin/jilin_plot.png" width="60%"/>

## How to Use

Jilin is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

Jilin is also available in Python through the key "*Network-Jilin*":
```python
network = load("Network-Jilin")
jilin_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Jilin.load).


## Reference

Bi, W. and Dandy, G.C., 2014. *Optimization of water distribution systems using online retrained metamodels*. Journal of
Water Resources Planning and Management, 140(11), p.04014032.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000419).
