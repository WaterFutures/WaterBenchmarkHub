---
title: "Fossolo"
id: "network-fossolo"
permalink: /benchmarks/network-Fossolo.html
collection: benchmarks
layout: benchmark
---


## Description

The Fossolo system is based on the Fossolo neighborhood distribution system in Bologna, Italy and was originally
developed by Bragalli et al. in 2008 as part of a design optimization study. The system has a total demand of 3,000 CMD,
one reservoir, and 8.4 km of pipe. It is classified as transmission dense-loop by Hwang & Lansey (2017) and looped by
Hoagland et al. (2015).

It was published 2016 by University of Kentucky Libraries.

The network consists of 36 nodes (junctions), 58 pipes and 1 reservoir.

<img src="../static/benchmarks/network-fossolo/fossolo_plot.png"/>

## How to Use

The Fossolo network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The Fossolo network is also available in Python through the key "*Network-Fossolo*":
```python
network = load("Network-Fossolo")
fossolo_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.Fossolo.load).


### Design Problem Description
Fossolo Network (FOS) includes fifty-eight pipes, thirty-six demand nodes, and one reservoir with a fixed head of 121.00 m. The material for all the pipes is polyethylene. Due to the feature of polyethylene, a relatively high roughness coefficient of 150 is applied to all the pipes. The minimum pressure head of all the demand nodes is maintained at 40 m, while the maximum pressure head of each node is specified in Table FOS.1. In addition, the flow velocity in each pipe is enforced to be less than or equal to 1 m/s. Table FOS.2 shows commercially available diameters and the corresponding unit costs.

#### Maximum Pressure Design Problem

Max Pressure:

<div id="Table FOS1"></div>
<script type="text/javascript">insertTable("Table FOS1", "../static/benchmarks/network-fossolo/FOS_Pressure.csv");</script>
<br>

#### Costs in the Network Design Problem

Diameter options and associdated costs:

<div id="Table FOS2"></div>
<script type="text/javascript">insertTable("Table FOS2", "../static/benchmarks/network-fossolo/FOS_Cost.csv");</script>
<br>


## Reference

Dandy, Graeme, "03 Fossolo" (2016). International Systems. 3.
[<i class="bi bi-link"></i>](https://uknowledge.uky.edu/wdst_international/3)

Bragalli, C. Ambrosio, D., Lee, J., Lodi, A., Toth, P. 2008. *IBM Research Report: Water Network Design by MINLP.* RC24495
(W0802-056)
[<i class="bi bi-link"></i>](https://dominoweb.draco.res.ibm.com/ef1b90113cc7b03a852573fc00529261.html)

Creaco, E. and Franchini, M. (2014) *Low level hybrid procedure for the multi-objective design of water distribution
networks*, Procedia Engineering 70, 369 – 378
[<i class="bi bi-link"></i>](https://doi.org/10.1016/j.proeng.2014.02.042)

Bi, W., Dandy, G. C. and Maier, H. R. (2015) *Improved genetic algorithm optimization of water distribution system design
by incorporating domain knowledge*, Environmental Modelling & Software, Vol. 69, 370-381.
[<i class="bi bi-link"></i>](https://doi.org/10.1016/j.envsoft.2014.09.010)
