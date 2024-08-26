---
title: "Nineteen Pipe"
id: "network-nineteen-pipe"
permalink: /benchmarks/network-Nineteen-Pipe.html
collection: benchmarks
layout: benchmark
---


## Description

The Nineteen Pipe system was created by Wood et al. in 1972 for use in computer modelling. The system has two reservoirs
and 5.2 miles of pipe. It is classified as distribution dense-grid by Hwang & Lansey (2017) and gridded by Hoagland et
al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 12 nodes (junctions), 21 pipes and 2 reservoirs.

<img src="../static/benchmarks/network-nineteen-pipe/nineteen_pipe_plot.png"/>

## How to Use

The Nineteen Pipe network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Nineteen Pipe network is also available in Python through the key "*Network-Nineteen-Pipe*":
```python
network = load("Network-Nineteen-Pipe")
nineteen_pipe_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.NineteenPipe.load).


## Reference

Hall, Ashley, "02 Nineteen Pipe" (2021). Historic Literature Systems. 5.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_systems/5)

Wood, Don J., Charles, Carl O. A. “*Hydraulic network analysis using linear theory.*” Journal of the hydraulics division,
Proceedings of the American Society of Civil Engineers (July 1972): 1157-1170.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/JYCEAJ.0003348)

Ormsbee, Lindell E., Wood, Don L. “*Hydraulic design algorithms for pipe networks.*” Journal of Hydraulic Engineering,
1986 112(12): 1195-1206.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)0733-9429(1986)112:12(1195))

