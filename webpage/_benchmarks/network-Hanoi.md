---
title: "Hanoi"
id: "network-hanoi"
permalink: /benchmarks/network-Hanoi.html
collection: benchmarks
layout: benchmark
---


## Description

The Hanoi system was first presented by Fujiwara and Khang (1990) and is based on the planned
trunk network of Hanoi, Vietnam. In subsequent years it became a widely used network in the
water research community -- e.g. it was used in the [LeakDB](KIOS-LeakDB.html) data set.

The network consists of 32 nodes (junctions), 34 pipes, and 1 reservoir.

<img src="../static/benchmarks/network-hanoi/hanoi_plot.png"/>

## How to Use

The Hanoi network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Hanoi network is also available in Python through the key "*Network-Hanoi*":
```python
network = load("Network-Hanoi")
hanoi_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Hanoi.load).


## Reference

Fujiwara, O. and Khang, D.B. (1990), A two-phase decomposition method for optimal
design of looped water distribution networks, Water Resour. Res., 26(4), 539-549.