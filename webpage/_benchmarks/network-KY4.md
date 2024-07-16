---
title: "KY4"
id: "network-ky4"
permalink: /benchmarks/network-KY4.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 4 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 1.51 MGD, one reservoir, four tanks, two pumps, and 162 miles of
pipe. It is classified as distribution sparse-grid by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 962 nodes (junctions), 1156 pipes, 4 tanks, 2 pumps and 1 reservoir.

<img src="../static/benchmarks/network-ky4/ky4_plot.png"/>

## How to Use

The KY4 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY4 network is also available in Python through the key "*Network-KY4*":
```python
network = load("Network-KY4")
ky4_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY4.load).


## Reference

Hoagland, Steven, "04 KY 4" (2016). Kentucky Dataset. 6.
https://uknowledge.uky.edu/wdst/6

Jolly, M. D., Lothes, A. D., Bryson, L. S., & Ormsbee, L. (2014). Research Database of Water Distribution System Models.
Journal of Water Resources Planning and Management, 410-416. 10.1061/(ASCE)WR.1943-5452.0000352
