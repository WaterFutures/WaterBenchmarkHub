---
title: "Anytown"
id: "network-anytown"
permalink: /benchmarks/network-Anytown.html
collection: benchmarks
layout: benchmark
---


## Description

The Anytown network was developed in the context of the [BWN](BWN.html) competition. Its main use consists in
researching network extensions.

The network consists of 19 junctions, 42 pipes, 1 pump and 3 reservoirs. It contains a demand pattern for 1 day.

<img src="../static/benchmarks/network-anytown/anytown_plot.png" width="50%"/>

## How to Use

Anytown is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

Anytown is also available in Python through the key "*Network-Anytown*":
```python
network = load("Network-Anytown")
anytown_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Anytown.load).


## Reference

Thomas M. Walski, E. Downey Brill, Jr., Johannes Gessler, Ian C. Goulter, Roland M. Jeppson,
Kevin Lansey, Han‐Lin Lee, Jon C. Liebman, Larry Mays, David R. Morgan,
and Lindell Ormsbee, (1987).
*Battle of the network models: Epilogue.*
Journal of Water Resources Planning and Management, 113(2), 191-203.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)0733-9496(1987)113:2(191))
