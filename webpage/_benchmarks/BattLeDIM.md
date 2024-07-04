---
title: "BattLeDIM (Battle of the Leakage Detection and Isolation Methods)"
id: "battledim"
permalink: /benchmarks/BattLeDIM.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of the Leakage Detection and Isolation Methods (*BattLeDIM*) is the 8th in a series
of "Battle Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.
It aims at objectively comparing the performance of methods for the detection and localization
of leakage events, relying on SCADA measurements of flow and pressure sensors installed within
water distribution networks.

The competition problem was based on [L-Town](network-LTown.html), a small hypothetical town which
experiences a large number of pipe breaks and water losses, affecting its service quality.
The [L-Town EPANET model](network-LTown.html) and the SCADA measurements provided were generated
based on a real water distribution network in a city in Cyprus.
Participants have been invited to use different tools and methods to detect and localize
the leakage events that occurred in L-Town in 2019, given the availability of a historical SCADA
dataset of the year 2018 and the evaluation SCADA dataset of the year 2019.
The teams, without knowing the solution to the problem, have submitted a results file indicating
the location and time of the detected leakages.

## How to Use

- [`L-Town.inp`](https://zenodo.org/records/4017659/files/L-TOWN.inp?download=1) EPANET Model (INP):
A model of the network is provided with nominal parameters for all the system elements. The nominal
base demands for each node are based on average historical metered consumption. In general, the
difference between the actual and the nominal values for each consumer type
(residential and commercial) is less than 10%. Weekly demand profiles for two consumer types
(residential and commercial) are also provided, however they do not capture the yearly seasonality.
Furthermore, the EPANET model parameters may be different from the actual network parameters
(e.g., diameters, roughness coefficients), and it is assumed than in general this difference is no
greater than 10% of the nominal values.
- [`2018 SCADA.xlsx`](https://zenodo.org/records/4017659/files/2018_SCADA.xlsx?download=1)
historical dataset: The historical data have been collected for the period 2018-01-01 00:00 until
2018-12-31 23:55, at 5-minute time steps. The SCADA dataset is comprised of the water tank level,
the flow sensors, the AMR measurements and the pressure sensors.
- [`2018 Leak Report.txt`](https://zenodo.org/records/4017659/files/2018_Fixed_Leakages_Report.txt?download=1):
The repair times of pipe bursts that have been fixed are provided.
- [`2018_Leakages.csv`](https://zenodo.org/records/4017659/files/2018_Leakages.csv?download=1):
Contains the leak demands at all leaky pipes over time in the historical data set.
This file was disclosed after the competition.
- [`L-TOWN_Real.inp`](https://zenodo.org/records/4017659/files/L-TOWN_Real.inp?download=1)
The L-Town network .inp file with realistic demand patterns -- this .inp file was used
for simulating the provided SCADA data. This file was disclosed after the competition.
- [`2019 SCADA.xlsx`](https://zenodo.org/records/4017659/files/2019_SCADA.xlsx?download=1)
evaluation Dataset: The evaluation data have been collected for the period 2019-01-01 00:00 until
2019-12-31 23:55, at 5-minute time steps. The SCADA dataset is comprised of the water tank level,
the flow sensors, the AMR measurements and the pressure sensors.
This dataset was used for the evaluation of the competing leakage detection methodologies,
and was disclosed in January 2020.
- [`2019_Leakages.csv`](https://zenodo.org/records/4017659/files/2019_Leakages.csv?download=1):
Contains the leak demands at all leaky pipes over time in the evaluation data set. This file was
disclosed after the competition.

The SCADA data contains the readings of 33 pressure sensors (in m), 1 water tank level sensor (in m),
3 flow sensors (in m^3/h), and 82 demand (AMR) sensors (in L/h).

### Usage in Python

This benchmark is also available in Python under the key "*BattLeDIM*":
```python
battledim = load("BattLeDIM")
```

Detailed information about the provided functionality can be found in the
[documentation](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.battledim.html).

## Reference

S. G. Vrachimis, D. G. Eliades, R. Taormina, Z. Kapelan, A. Ostfeld, S. Liu, M. Kyriakou, P. Pavlou,
M. Qiu, and M. M. Polycarpou. Forthcoming. *Battle of the Leakage Detection and Isolation Methods*,
Journal of Water Resources Planning and Management, 10.1061/(ASCE)WR.1943-5452.0001601