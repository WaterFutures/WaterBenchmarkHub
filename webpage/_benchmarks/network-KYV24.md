---
title: "KYV24"
id: "network-kyv24"
permalink: /benchmarks/network-KYV24.html
collection: benchmarks
layout: benchmark
---


## Description

The KY V24 system is based on a real-world system in KY and was originally used by Hernandez & Ormsbee in 2020 as part
of a classification study. The system has a total demand of 0.13 MGD, two reservoirs, and 52.6 miles of pipe. It is
classified as distribution branch by Hwang & Lansey (2017) and branched by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 202 nodes (junctions), 249 pipes and 2 tanks.

<img src="../static/benchmarks/network-kyv24/kyv24_plot.png"/>

## How to Use

The KYV24 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KYV24 network is also available in Python through the key "*Network-KYV24*":
```python
network = load("Network-KYV24")
kyv24_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KYV24.load).


## Reference

Hernandez Hernandez, Erika, "09 KY V24" (2021). Kentucky Valved Dataset. 9.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_ky_valved/9)

Hernandez Hernandez, Erika, and Ormsbee, Lindell. "*Segment-Based Assessment of Consequences of Failure on Water
Distribution Systems.*" Journal of Water Resources Planning and Management 147.4 (2021): 04021009.
10.1061/(ASCE)WR.1943-5452.0001340
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001340)
