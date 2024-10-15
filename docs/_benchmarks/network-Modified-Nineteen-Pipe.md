---
title: "Modified Nineteen Pipe"
id: "network-modified-nineteen-pipe"
permalink: /benchmarks/network-Modified-Nineteen-Pipe.html
collection: benchmarks
layout: benchmark
---


## Description

The Modified Nineteen Pipe system was created by Ormsbee & Contractor in 1981 and is based on the [Nineteen Pipe System](network-Nineteen-Pipe.md).
The system has a total demand of 3.1 MGD, two reservoirs and 6.25 miles of pipe. It is classified as distribution
dense-grid by Hwang & Lansey (2017) and gridded by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 12 nodes (junctions), 21 pipes and 2 reservoirs.

<img src="../static/benchmarks/network-modified-nineteen-pipe/modified_nineteen_pipe_plot.png"/>

## How to Use

The Modified Nineteen Pipe network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Nineteen Pipe network is also available in Python through the key "*Network-Modified-Nineteen-Pipe*":
```python
network = load("Network-Modified-Nineteen-Pipe")
modified_nineteen_pipe_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.ModifiedNineteenPipe.load).


## Reference

Ormsbee, Lindell E., "04 Modified Nineteen Pipe" (2021). Historic Literature Systems. 7.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_systems/7)

Ormsbee, L.E. and Contractor, D.N., 1981, July. Optimization of hydraulic networks. In International Symposium on Urban
Hydrology, Hydraulics, and Sediment Control, Kentucky, Lexington, KY (pp. 255-261).
