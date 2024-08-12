---
title: "KY6"
id: "network-ky6"
permalink: /benchmarks/network-KY6.html
collection: benchmarks
layout: benchmark
---


## Description

The KY 6 system is based on a real-world system in KY and was originally used by Jolly et al. in 2014 as part of a
classification study. The system has a total demand of 1.56 MGD, two reservoirs, three tanks, two pumps, and 58.5 miles
of pipe. It is classified as distribution dense-grid by Hwang & Lansey (2017) and looped by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 537 nodes (junctions), 644 pipes, 1 valve, 3 tanks, 2 pumps and 2 reservoirs.

<img src="../static/benchmarks/network-ky6/ky6_plot.png"/>

## How to Use

The KY6 network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The KY6 network is also available in Python through the key "*Network-KY6*":
```python
network = load("Network-KY6")
ky6_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KY6.load).


## Reference

Hoagland, Steven, "06 KY 6" (2016). Kentucky Dataset. 8.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst/8)

Jolly, M. D., Lothes, A. D., Bryson, L. S., & Ormsbee, L. (2014). *Research Database of Water Distribution System Models.*
Journal of Water Resources Planning and Management, 410-416. 10.1061/(ASCE)WR.1943-5452.0000352
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000352)
