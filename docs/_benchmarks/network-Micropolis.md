---
title: "Micropolis"
id: "network-micropolis"
permalink: /benchmarks/network-Micropolis.html
collection: benchmarks
layout: benchmark
---


## Description

Micropolis is a virtual city designed to research critical infrastructure and be able to publish the results.

The network consists of 1574 junctions, 1823 pipes, 2 reservoirs, 1 tank and 8 pumps. It contains a demand pattern for
1 week and 3 days.

<img src="../static/benchmarks/network-micropolis/micropolis_plot.png" width="100%"/>

## How to Use

Micropolis is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

Micropolis is also available in Python through the key "*Network-Micropolis*":
```python
network = load("Network-Micropolis")
micropolis_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Micropolis.load).


## Reference

Brumbelow, K., Torres, J., Guikema, S., Bristow, E. and Kanta, L., 2007. Virtual cities for water distribution and
infrastructure system research. In World environmental and water resources congress 2007: Restoring our natural habitat
(pp. 1-7).
[<i class="bi bi-link"></i>](https://doi.org/10.1061/40927(243)469)
