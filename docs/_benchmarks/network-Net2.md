---
title: "Net2"
id: "network-net2"
permalink: /benchmarks/network-Net2.html
collection: benchmarks
layout: benchmark
---


## Description

The EPANET Example Network 2 (short `Net2`) constitutes a simple example of modeling chlorine decay.
Both bulk and wall reactions are included.

The network consists of 35 junctions, 40 pipes and 1 tank. It contains a demand pattern for 2 days and 7 hours.

<img src="../static/benchmarks/network-net2/net2_plot.png"/>

## How to Use

Net2 is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

Net2 is also available in Python through the key "*Network-Net2*":
```python
network = load("Network-Net2")
net2_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Net2.load).


## Reference

Rossman, Lewis A., Robert M. Clark, and Walter M. Grayman. "Modeling chlorine residuals in drinking-water distribution systems." Journal of environmental engineering 120.4 (1994): 803-820.
[<i class="bi bi-link"></i>](http://dx.doi.org/10.1061/(ASCE)0733-9372(1994)120:4(803))

Rossman, L. A. (2000). *EPANET 2: users manual.*
[<i class="bi bi-link"></i>](https://www.engr.colostate.edu/CIVE572/Projects/PROJ%202-Urban%20Water%20Dist%20System%20Analysis/EN2manual.pdf)
