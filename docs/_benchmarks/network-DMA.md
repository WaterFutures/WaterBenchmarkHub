---
title: "DMA"
id: "network-dma"
permalink: /benchmarks/network-DMA.html
collection: benchmarks
layout: benchmark
---


## Description

The Demand Management Areas system is based on a real-world system and was presented by Saldarriga et al. in 2016 as
part of a Battle of the Networks ([BWNDMA](BWNDMA.html)) to optimize district metering areas. The system has a total demand of 3110 CMD, five
reservoirs, three pumps, 17 tanks, and 872 km of pipe. It is classified as distribution sparse-grid by Hwang & Lansey
(2017) and gridded by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

The network consists of 11063 nodes (junctions), 13930 pipes, 17 tanks, 3 pumps and 5 reservoirs.

<img src="../static/benchmarks/network-dma/dma_plot.png" width="100%"/>

## How to Use

The DMA network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The DMA network is also available in Python through the key "*Network-DMA*":
```python
network = load("Network-DMA")
dma_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.DMA.load).


## Reference

Ostfeld, Avi, "06 Demand Management Areas" (2021). Battle of the Water Network Models. 6.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_models/6)

Juan Saldarriaga, Jessica Bohorquez, David Celeita, Laura Vega, Diego Paez, Dragan Savic,
Graeme Dandy, Yves Filion, Walter Grayman, and Zoran Kapelan (2019).
*Battle of the water networks district metered areas.*
Journal of Water Resources Planning and Management, 145(4)
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001035)