---
title: "BWSN-1"
id: "network-bwsn1"
permalink: /benchmarks/network-BWSN-1.html
collection: benchmarks
layout: benchmark
---


## Description

The BWSN-1 network is an artifical network that was first
introduced in the [BWSN competition](BWSN.html) in 2006 together with the
much larger [BWSN-2 network](network-BWSN-2.html).

The network consists of 126 junctions, 154 pipes, 1 reservoir, 2 tanks,
2 pumps, and 8 valves.
Furthermore, it also contains a really simple demand pattern for 4 days.


<img src="../static/benchmarks/network-bwsn/bwsn1_plot.png"/>

## How to Use

BWSN-1 is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

BWSN-1 is also available in Python through the key "*Network-BWSN-1*":
```python
network = load("Network-BWSN-1")
bwsn1_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.BWSN1.load).


## Reference

Avi Ostfeld, James G. Uber, Elad Salomons, Jonathan W. Berry, William E. Hart, Cindy A. Phillips,
Jean-Paul Watson, Gianluca Dorini, Philip Jonkergouw, Zoran Kapelan, Francesco di Pierro,
Soon-Thiam Khu, Dragan Savic, Demetrios Eliades, Marios Polycarpou, Santosh R. Ghimire,
Brian D. Barkdoll, Roberto Gueli, Jinhui J. Huang, Edward A. McBean, William James, Andreas Krause,
Jure Leskovec, Shannon Isovitsch, Jianhua Xu, Carlos Guestrin, Jeanne VanBriesen, Mitchell Small,
Paul Fischbeck, Ami Preis, Marco Propato, Olivier Piller, Gary B. Trachtman, Zheng Yi Wu,
and Tom Walski. (2008).
*The battle of the water sensor networks (BWSN): A design challenge for engineers and algorithms.*
Journal of water resources planning and management, 134(6).
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)0733-9496(2008)134:6(556))
