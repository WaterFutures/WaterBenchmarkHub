---
title: "KYALL"
id: "network-ky-all"
permalink: /benchmarks/network-KYALL.html
collection: benchmarks
layout: benchmark
---


## Description

The KY-ALL system is based on the entire water distribution system in Kentucky and was originally published by Luke Butler as part of a
performance stress testing of *epanet-js*.

The network consists of 317947 nodes (junctions), 352378 pipes, 2653 tanks, 4703 pump and 2653 reservoir.

<figure>
<img src="../static/benchmarks/network-kyall/kyall_map_plot.jpg"/>
<figcaption><small>Screenshot from epanet-js</small></figcaption>
</figure>


## How to Use

The KY-ALL Network is provided as an .inp file and can be loaded into EPANET or any other software package supporting .inp files.

### Usage in Python

KY-ALL is also available in Python through the key "*Network-Ky-All*":
```python
network = load("Network-Ky-All")
kyall_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.KYALL.load).


## Reference

Luke Butler, *epanet-js* (2026)
