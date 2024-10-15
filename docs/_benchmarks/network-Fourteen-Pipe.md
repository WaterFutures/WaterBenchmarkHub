---
title: "Fourteen Pipe"
id: "network-fourteen-pipe"
permalink: /benchmarks/network-Fourteen-Pipe.html
collection: benchmarks
layout: benchmark
---


## Description

The Fourteen Pipe system is a simple example system originally used by Gessler & Walski in 1985 to test pipe size
optimization software. The system has a total demand of 12,100 CMD, two reservoirs and 30.6 km of pipe and is classified
as distribution dense-grid by Hwang & Lansey (2017) and gridded by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 10 nodes (junctions), 14 pipes and 2 reservoirs.

<img src="../static/benchmarks/network-fourteen-pipe/fourteen_pipe_plot.png"/>

## How to Use

The Fourteen Pipe network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Fourteen Pipe network is also available in Python through the key "*Network-Fourteen-Pipe*":
```python
network = load("Network-Fourteen-Pipe")
fourteen_pipe_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.FourteenPipe.load).


## Reference

Hall, Ashley, "06 Fourteen Pipe" (2021). Historic Literature Systems. 9.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_systems/9)

Gessler, J. and Walski, T.M. (1985) *Water distribution system optimization*, US Army corps of engineers waterways
experimentation station, Technical Report TR EL-85-11, Vicksburg, Miss.
[<i class="bi bi-link"></i>](http://hdl.handle.net/11681/10103)
