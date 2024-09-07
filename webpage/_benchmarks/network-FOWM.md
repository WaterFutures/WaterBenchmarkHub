---
title: "FOWM"
id: "network-fowm"
permalink: /benchmarks/network-FOWM.html
collection: benchmarks
layout: benchmark
---


## Description

The Federally Owned Water Main system is a skeletonized version of the water distribution system servicing northern
Arlington County, VA. It was originally used by Walski in 1985 to evaluate the resilience of the network. The system
has a total demand of 3.2 MGD, one reservoir and 16.7 miles of pipe. It is classified as transmission branch by Hwang
& Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 45 nodes (junctions), 49 pipes, and 1 reservoir.

<img src="../static/benchmarks/network-fowm/fowm_plot.png"/>

## How to Use

The FOWM network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The CA1 network is also available in Python through the key "*Network-FOWM*":
```python
network = load("Network-FOWM")
fowm_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.FOWM.load).


## Reference

Walski, Thomas M., "05 Federally Owned Water Main" (2021). Historic Literature Systems. 8.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_systems/8)

Walski, T.M. 1984. “*Application of Procedures for Testing and Evaluating Water Distribution Systems*,” Technical Report
EL-84-5, U.S. Army Engineer Waterways Experiment Station, CE, Vicksburg, Miss.
[<i class="bi bi-link"></i>](https://apps.dtic.mil/sti/tr/pdf/ADA144558.pdf)

Chase, Donald V.; Ormsbee, Lindell; and Walski, Thomas M., "*Technical Report EL-88-18: Reliability of the Federally
Owned Water Main System*" (1988). Civil and Environmental Engineering and Engineering Mechanics Faculty Publications. 15.
[<i class="bi bi-link"></i>](https://ecommons.udayton.edu/cee_fac_pub/15)
