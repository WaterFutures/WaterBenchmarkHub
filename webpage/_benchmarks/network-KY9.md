---
title: "KY9"
id: "network-ky9"
permalink: /benchmarks/network-KY9.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 9 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 1.38 MGD, four reservoirs, 15 tanks, 17 pumps, and 594 miles of
pipe. It is classified as distribution branch by Hwang & Lansey (2017) and branched by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 1096 nodes (junctions), 1270 pipes, 15 tanks, 17 pumps and 4 reservoirs.

<img src="../static/benchmarks/network-ky9/ky9_plot.png"/>

## How to Use

The KY9 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY9 network is also available in Python through the key "*Network-KY9*":
```python
network = load("Network-KY9")
ky9_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY9.load).


## Reference

Hoagland, Steven, "09 KY 9" (2016). Kentucky Dataset. 11.
https://uknowledge.uky.edu/wdst/11

Jolly, M. D., Lothes, A. D., Bryson, L. S., & Ormsbee, L. (2014). Research Database of Water Distribution System Models.
Journal of Water Resources Planning and Management, 410-416. 10.1061/(ASCE)WR.1943-5452.0000352
