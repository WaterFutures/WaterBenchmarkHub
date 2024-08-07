---
title: "KY13"
id: "network-ky13"
permalink: /benchmarks/network-KY13.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 13 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 2.7 MGD, two reservoirs, seven tanks, four pumps, and 95 miles of
pipe and is classified as distribution sparse-grid by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 770 nodes (junctions), 940 pipes, 5 tanks, 4 pumps and 2 reservoirs.

<img src="../static/benchmarks/network-ky13/ky13_plot.png"/>

## How to Use

The KY13 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY13 network is also available in Python through the key "*Network-KY13*":
```python
network = load("Network-KY13")
ky13_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY13.load).


## Reference

Hoagland, Steven, "13 KY 13" (2016). Kentucky Dataset. 15.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst/15)

Schal, S., Bryson, L.S. and Ormsbee, L., 2014. A graphical procedure for sensor-placement guidance for small utilities.
Journal-American Water Works Association, 106(10), pp.E459-E469.
[<i class="bi bi-link"></i>](https://doi.org/10.5942/JAWWA.2014.106.0093)
