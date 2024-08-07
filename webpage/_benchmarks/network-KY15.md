---
title: "KY15"
id: "network-ky15"
permalink: /benchmarks/network-KY15.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 15 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 1.50 MGD, two reservoirs, 8 tanks, 16 pumps, and 300 miles of
pipe. It is classified as distribution branch by Hwang & Lansey (2017) and branched by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 582 nodes (junctions), 671 pipes, 28 valves, 8 tanks, 13 pumps and 2 reservoirs.

<img src="../static/benchmarks/network-ky15/ky15_plot.png"/>

## How to Use

The KY15 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY15 network is also available in Python through the key "*Network-KY15*":
```python
network = load("Network-KY15")
ky15_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY15.load).


## Reference

Hoagland, Steven, "15 KY 15" (2016). Kentucky Dataset. 17.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst/17)

Schal, S., Bryson, L.S. and Ormsbee, L., 2014. A graphical procedure for sensor-placement guidance for small utilities.
Journal-American Water Works Association, 106(10), pp.E459-E469.
[<i class="bi bi-link"></i>](https://doi.org/10.5942/JAWWA.2014.106.0093)
