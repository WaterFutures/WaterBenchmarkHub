---
title: "KY8"
id: "network-ky8"
permalink: /benchmarks/network-KY8.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 8 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 2.47 MGD, two reservoirs, five tanks, four pumps, and 150 miles
of pipe. It is classified as distribution sparse-grid by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 1317 nodes (junctions), 1614 pipes, 5 tanks, 4 pumps and 2 reservoirs.

<img src="../static/benchmarks/network-ky8/ky8_plot.png"/>

## How to Use

The KY8 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY8 network is also available in Python through the key "*Network-KY8*":
```python
network = load("Network-KY8")
ky8_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY8.load).


## Reference

Hoagland, Steven, "08 KY 8" (2016). Kentucky Dataset. 10.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst/10)

Jolly, M. D., Lothes, A. D., Bryson, L. S., & Ormsbee, L. (2014). *Research Database of Water Distribution System Models.*
Journal of Water Resources Planning and Management, 410-416. 10.1061/(ASCE)WR.1943-5452.0000352
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000352)
