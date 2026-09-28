---
title: "02-us-style Network" 
id: "network-02-us-style"
permalink: /benchmarks/network-02-us-style.html
collection: benchmarks
layout: benchmark  
---

## Description

The `02-us-style Network` is a demo example network provided by **epanet.js**. It is located in Canada. 

The network consists of 128 nodes, 166 pipes, 1 valve, 2 reservoirs and 1 tank. 

<img src="../static/benchmarks/network-02-us-style/02-us-style_plot.png"/>

## How to Use

The 02-us-style Network is provided as an .inp file and can be loaded into EPANET or any other software package supporting .inp files.

### Usage in Python

02-us-style is also available in Python through the key "*Network-US-Style*":
```python
network = load("Network-US-Style")
usstyle_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.USStyle.load).


## Reference
Example model provided by *epanet.js*: [<i class="bi bi-link"></i>](https://github.com/epanet-js/epanet-js/blob/main/public/example-models/02-us-style.inp)