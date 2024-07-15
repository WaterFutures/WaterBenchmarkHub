---
title: "KY1"
id: "network-ky1"
permalink: /benchmarks/network-KY1.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 1 system is based on a real-world system in KY and was originally used by Hoagland in 2015 as part of a
classification study. The system has a total demand of 2.0 MGD, one reservoir, two tanks, and 40.6 miles of pipe. It is
classified as distribution sparse-grid by Hwang & Lansey (2017) and gridded by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 854 nodes (junctions), 984 pipes, 2 tanks, 1 pump and 1 reservoir.

<img src="../static/benchmarks/network-ky1/ky1_plot.png"/>

## How to Use

The KY1 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY1 network is also available in Python through the key "*Network-KY1*":
```python
network = load("Network-KY1")
ky1_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY1.load).


## Reference

Hoagland, Steven, "01 KY 1" (2016). Kentucky Dataset. 3.
https://uknowledge.uky.edu/wdst/3

Hoagland, Steven & Schal, Stacey & Ormsbee, Lindell & Bryson, Lindsey. (2015). Classification of Water Distribution
Systems for Research Applications. 696-702. 10.1061/9780784479162.064.
