---
title: "Two-Reservoir Network (TRN)"
id: "network-trn"
permalink: /benchmarks/network-TRN.html
collection: benchmarks
layout: benchmark
---

## Description

The synthetic Two-Reservoir Network (TRN) was created as a network design problem.

The network consists of 10 nodes, 17 pipes and 2 reservoirs.

<img width="50%" src="../static/benchmarks/network-trn/trn_plot.png"/>

## How to Use

The TRN network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

## Network Design Problem

Minimum pressure requirement of each node under the three demand patterns:

<div id="tab-pressure-req"></div>
<script type="text/javascript">insertTable("tab-pressure-req", "../static/benchmarks/network-trn/trn-design_problem-min_pressure_req.csv");</script>
<br>

Diameter options and associdated costs:

<div id="tab-diameter-costs"></div>
<script type="text/javascript">insertTable("tab-diameter-costs", "../static/benchmarks/network-trn/trn-design_problem-unit_costs.csv");</script>
<br>


### Usage in Python

The TRN network is also available in Python through the key "*Network-TRN*":
```python
network = load("Network-TRN")
tln_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.TRN.load).


## Reference

Gessler, J. (1985). *Pipe network optimization by enumeration.* In Computer applications in water resources (pp. 572-581). ASCE.
