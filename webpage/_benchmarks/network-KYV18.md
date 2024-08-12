---
title: "KYV18"
id: "network-kyv18"
permalink: /benchmarks/network-KYV18.html
collection: benchmarks
layout: benchmark
---


## Description

The KY V18 system is based on a real-world system in KY and was originally used by Hernandez & Ormsbee in 2020 as part
of a classification study. The system has a total demand of 2.2 MGD, one reservoir, three tanks, three pumps, and 112
miles of pipe. It is classified as distribution sparse-grid by Hwang & Lansey (2017) and Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 1233 nodes (junctions), 1378 pipes, 3 tanks, 3 pumps and 1 reservoir. It contains a demand
pattern for 10 hours.

<img src="../static/benchmarks/network-kyv18/kyv18_plot.png" width="100%"/>

## How to Use

The KYV18 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KYV18 network is also available in Python through the key "*Network-KYV18*":
```python
network = load("Network-KYV18")
kyv18_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KYV18.load).


## Reference

Hernandez Hernandez, Erika, "03 KY V18" (2021). Kentucky Valved Dataset. 3.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_ky_valved/3)

Hernandez Hernandez, Erika, and Ormsbee, Lindell. "*Segment-Based Assessment of Consequences of Failure on Water
Distribution Systems.*" Journal of Water Resources Planning and Management 147.4 (2021): 04021009.
10.1061/(ASCE)WR.1943-5452.0001340
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001340)
