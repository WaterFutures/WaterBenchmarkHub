---
title: "KY12"
id: "network-ky12"
permalink: /benchmarks/network-KY12.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 12 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 1.38 MGD, one reservoir, seven tanks, 15 pumps, and 399 miles of
pipe. It is classified as distribution branch by Hwang & Lansey et al. (2017) and branched by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 2273 nodes (junctions), 2426 pipes, 22 valves, 7 tanks, 15 pumps and 1 reservoir.

<img src="../static/benchmarks/network-ky12/ky12_plot.png" width="100%"/>

## How to Use

The KY12 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY12 network is also available in Python through the key "*Network-KY12*":
```python
network = load("Network-KY12")
ky12_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY12.load).


## Reference

Hoagland, Steven, "11 KY 11" (2016). Kentucky Dataset. 13.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst/13)

Jolly, M. D., Lothes, A. D., Bryson, L. S., & Ormsbee, L. (2014). *Research Database of Water Distribution System Models.*
Journal of Water Resources Planning and Management, 410-416. 10.1061/(ASCE)WR.1943-5452.0000352
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000352)
