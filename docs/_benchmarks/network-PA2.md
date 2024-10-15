---
title: "PA2"
id: "network-pa2"
permalink: /benchmarks/network-PA2.html
collection: benchmarks
layout: benchmark
---


## Description

The PA 2 system is based on a portion of the Cheshire Distribution system near Harrisburg, PA and was originally
developed by Vasconcelos et al. in 1997 as part of a water quality modelling study. The system has a total demand of
1.1 MGD, one reservoir, one pump, and 11.3 miles of pipe. It is classified as distribution branch by Hwang & Lansey
(2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 262 nodes (junctions), 290 pipes, 1 pump and 1 reservoir. It contains a demand pattern for 1
day and 11 hours.

<img src="../static/benchmarks/network-pa2/pa2_plot.png"/>

## How to Use

The PA2 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The PA2 network is also available in Python through the key "*Network-PA2*":
```python
network = load("Network-PA2")
pa2_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.PA2.load).


## Reference

Boccelli, Dominic L., "03 PA 2" (2016). US Systems. 3.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_us/3)

Vasconcelos, J.J., Rossman, L.A., Grayman, W.M., Boulos, P.F. and Clark, R.M., 1997. *Kinetics of chlorine decay.*
Journal-American Water Works Association, 89(7), pp.54-65. 
[<i class="bi bi-link"></i>](https://doi.org/10.1002/j.1551-8833.1997.tb08259.x)
