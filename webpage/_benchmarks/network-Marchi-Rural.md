---
title: "Marchi Rural"
id: "network-marchi-rural"
permalink: /benchmarks/network-Marchi-Rural.html
collection: benchmarks
layout: benchmark
---


## Description

The Marchi Rural system is based on an irrigation system in Australia and was originally developed by Marchi et al. in
2014 as part of a design optimization study. The system has a total demand of 5,600 CMD, two reservoirs, and 1,288 km of
pipe. It is classified as transmission dense-loop by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 379 nodes (junctions), 476 pipes and 2 reservoirs.

<img src="../static/benchmarks/network-marchi-rural/marchi_rural_plot.png"/>

## How to Use

The Marchi Rural network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Marchi Rural network is also available in Python through the key "*Network-Marchi-Rural*":
```python
network = load("Network-Marchi-Rural")
marchi_rural_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.MarchiRural.load).


## Reference

Dandy, Graeme, "07 Marchi Rural" (2016). International Systems. 7.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_international/7)

Marchi, A., Dandy, G., Wilkins, A. and Rohrlach, H., 2014. *Methodology for comparing evolutionary algorithms for
optimization of water distribution systems.* Journal of water resources planning and management, 140(1), pp.22-31.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000321)

Bi, W., Dandy, G. C. and Maier, H. R. (2015) *Improved genetic algorithm optimization of water distribution system design
by incorporating domain knowledge*, Environmental Modelling & Software, Vol. 69, 370-381.
[<i class="bi bi-link"></i>](https://doi.org/10.1016/j.envsoft.2014.09.010)
