---
title: "KYV22"
id: "network-kyv22"
permalink: /benchmarks/network-KYV22.html
collection: benchmarks
layout: benchmark
---


## Description

The KY V22 system is based on a real-world system in KY and was originally used by Hernandez & Ormsbee in 2020 as part
of a classification study. The system has a total demand of 0.52 MGD, one reservoir, seven tanks, four pump, and 33.2
miles of pipe. It is classified as distribution branch by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 687 nodes (junctions), 733 pipes, 7 tanks, 4 pumps and 1 reservoir.

<img src="../static/benchmarks/network-kyv22/kyv22_plot.png"/>

## How to Use

The KYV22 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KYV22 network is also available in Python through the key "*Network-KYV22*":
```python
network = load("Network-KYV22")
kyv22_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KYV22.load).


## Reference

Hernandez Hernandez, Erika, "07 KY V22" (2021). Kentucky Valved Dataset. 7.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_ky_valved/7)

Hernandez Hernandez, Erika, and Ormsbee, Lindell. "*Segment-Based Assessment of Consequences of Failure on Water
Distribution Systems.*" Journal of Water Resources Planning and Management 147.4 (2021): 04021009.
10.1061/(ASCE)WR.1943-5452.0001340
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001340)
