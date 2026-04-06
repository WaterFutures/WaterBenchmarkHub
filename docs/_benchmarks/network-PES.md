---
title: "Pescara"
id: "network-PES"
permalink: /benchmarks/network- Pescara.html
collection: benchmarks
layout: benchmark
---

## Description

The Pescara system is based on the water distribution system in Pescara, Italy and was originally developed by Bragalli et al. in 2008 as part of a design optimization study. The system has a total demand of 57,000 CMD, three reservoirs, and 49 km of pipe. It is classified as distribution dense-grid by Hwang & Lansey (2017) and gridded by Hoagland et al. (2015).

It was published 2021 by University of Kentucky Libraries.

Pescara Network (PES) includes ninety-nine pipes, sixty-eight demand nodes, and three reservoirs with fixed head within 53.08 m to 57.00 m. The pipe material is cast iron. A uniform Hazen-Williams roughness coefficient of 130 is applied to all pipes. 

<img src="../static/benchmarks/network- Pescara/PES.png"/>

### Design Problem Description

The minimum pressure head of all the demand nodes is maintained at 20 m, while the maximum pressure head of each node is specified in Table PES.1. In addition, the flow velocity in each pipe is enforced to be less than or equal to 2 m/s. Table PES.2 shows commercially available diameters and the corresponding unit costs.

#### Maximum Pressure Design Problem

Max Pressure:

<div id="Table PES1"></div>
<script type="text/javascript">insertTable("Table PES1", "../static/benchmarks/network- Pescara/PES_Pressure.csv");</script>
<br>

#### Costs in the Network Design Problem

Diameter options and associdated costs:

<div id="Table PES2"></div>
<script type="text/javascript">insertTable("Table PES2", "../static/benchmarks/network- Pescara/PES_Cost.csv");</script>
<br>


## Reference
Hall, Ashley, "04 Pescara" (2021). International Systems. 4.
https://uknowledge.uky.edu/wdst_international/4



