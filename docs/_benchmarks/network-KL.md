---
title: "KL"
id: "network-kl"
permalink: /benchmarks/network-KL.html
collection: benchmarks
layout: benchmark
---


## Description

The KL network was designed in 2012 by Kang and Lansey in order to study WDN optimization.

The network consists of 935 junctions, 1274 pipes and 1 reservoir.

<img src="../static/benchmarks/network-kl/kl_plot.png" width="100%"/>

## How to Use

KL is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

KL is also available in Python through the key "*Network-KL*":
```python
network = load("Network-KL")
kl_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KL.load).


## Reference

Kang, D. and Lansey, K., 2012. *Revisiting optimal water-distribution system design: issues and a heuristic hierarchical
approach*. Journal of Water resources planning and management, 138(3), pp.208-217.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000165)
