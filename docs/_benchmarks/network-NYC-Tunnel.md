---
title: "New York City Tunnel"
id: "network-nyc-tunnel"
permalink: /benchmarks/network-NYC-Tunnel.html
collection: benchmarks
layout: benchmark
---


## Description

The New York Tunnel system is based on the real-world transmission system in New York City and was created by Schaake &
Lai in 1969 as part of a study to optimize the duplication of the existing system to meet demand increases. The system
has a total demand of 1305 MGD, one reservoir and 21 tunnels with a total length of 69.2 miles. It is classified as
distribution dense-grid by Hwang & Lansey (2017) and gridded by Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 19 nodes (junctions), 42 pipes and 1 reservoir. It contains a demand pattern for 3 days.

<img src="../static/benchmarks/network-nyc-tunnel/nyc_tunnel_plot.png"/>

## How to Use

The New York City Tunnel network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The New York City Tunnel network is also available in Python through the key "*Network-NYC-Tunnel*":
```python
network = load("Network-NYC-Tunnel")
nyc_tunnel_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.NYC_Tunnel.load).


## Reference

Dandy, Graeme, "01 New York Tunnel" (2016). Historic Literature Systems. 1.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_systems/1)

Schaake, J.C. and Lai, D. (1969) *Linear programming and dynamic programming applications to water distribution network
design*, Report 116, Hydrodyn. Lab., Dep. of Civil Eng., MIT, Cambridge, Mass.
[<i class="bi bi-link"></i>](https://dspace.mit.edu/handle/1721.1/143047)

Dandy, G., Simpson, A., & Murphy, L. (1996). *An Improved Genetic Algorithm for Pipe Network Optimization*. Water
Resources Research., 32(2), 449-458.
[<i class="bi bi-link"></i>](https://doi.org/10.1029/95WR02917)

Fujiwara, O., & Khang, D. (1990). *A two-phase decomposition method for optimal design of looped water distribution
networks*. Water Resources Research., 26(4), 539-549.
[<i class="bi bi-link"></i>](https://doi.org/10.1029/WR026i004p00539)

Morgan, D., & Goulter, I. (1985). *Optimal urban water distribution design*. Water Resources Research., 21(5), 642-652.
[<i class="bi bi-link"></i>](https://doi.org/10.1029/WR021i005p00642)
