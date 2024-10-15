---
title: "KYV8"
id: "network-kyv8"
permalink: /benchmarks/network-KYV8.html
collection: benchmarks
layout: benchmark
---


## Description

The KY V8 system is based on a real-world system in KY and was originally used by Hernandez & Ormsbee in 2020 as part
of a classification study. The system has a total demand of 2.47 MGD, two reservoirs, five tanks, four pumps, and 150
miles of pipe. It is classified as distribution branch by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries. A non valved version is available at [KY8](network-KY8.html).

The network consists of 2439 nodes (junctions), 3221 pipes, 488 valves, 5 tanks, 4 pumps and 2 reservoirs. It contains a demand
pattern for one day.

<img src="../static/benchmarks/network-kyv8/kyv8_plot.png" width="100%"/>

## How to Use

The KYV8 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KYV8 network is also available in Python through the key "*Network-KYV8*":
```python
network = load("Network-KYV8")
kyv8_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KYV8.load).


## Reference

Hernandez Hernandez, Erika, "02 KY V8" (2021). Kentucky Valved Dataset. 2.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_ky_valved/2)

Hernandez Hernandez, Erika, and Ormsbee, Lindell. "*Segment-Based Assessment of Consequences of Failure on Water
Distribution Systems.*" Journal of Water Resources Planning and Management 147.4 (2021): 04021009.
10.1061/(ASCE)WR.1943-5452.0001340
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001340)
