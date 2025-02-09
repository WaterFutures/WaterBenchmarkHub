---
title: "LeakG3PD: A Python Generator and Simulated Water Distribution System Dataset"
id: "leakg3pd"
permalink: /benchmarks/LeakG3PD.html
collection: benchmarks
layout: benchmark
---


## Description

LeakG3PD constitutes an updated and extended version of [LeakDB](KIOS-LeakDB.html).
The main differences are the following:
- Leak data consistency: Leak demands track pressure values according to the [WNTR](https://github.com/USEPA/WNTR) leak model equation.
- In addition to [Hanoi](network-Hanoi.html) and [Net1](network-Net1.html), [Net3](network-Net3.html) is also included.
- More realistic representations of possible leak locations: Leaks are represented as new nodes inserted within random points along random pipes.
- More variability of physical values during time: Demand patterns for different nodes are time shifted of up to 2h with 30min intervals; demand patterns have value 0 at random times.
- Improved storage features: Files for diferent nodes and links are grouped into single archives according to physical variables; the only scenario without any leak during the entire simulation time is scenario 0.

## How to Use

Different from the original [LeakDB](KIOS-LeakDB.html), the benchmark contains only 500 scenarios
for each network.
For each scenario, the pressure, demands, and flow rates at every node/link in the
network are provided as .csv files. The leakage location and type (abrupt, incipient) are provided
as well (see ```Leaks``` folder) -- note that not every scenario contains leakages.
Furthermore, the .inp file used for the simulation is available as well.
Labels for each time step (30-minute steps) indicating the presence of a leak
are given in ```Labels.csv```.


## Reference

Pilotto Figueiredo, M., de Souza Oliveira, L., Lucca, G., Correa Yamin, A.,
Huckembeck dos Santos, W., da Rosa Lopes, T. (2025).
*LeakG3PD: A Python Generator and Simulated Water Distribution System Dataset.*
In: Julian, V., et al. Intelligent Data Engineering and Automated Learning -- IDEAL 2024
[<i class="bi bi-link"></i>](https://doi.org/10.1007/978-3-031-77738-7_7)