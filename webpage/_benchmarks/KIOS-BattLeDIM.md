---
title: "BattLeDIM (Battle of the Leakage Detection and Isolation Methods)"
id: "kios-battledim"
permalink: /benchmarks/KIOS-BattLeDIM.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of the Leakage Detection and Isolation Methods (*BattLeDIM*) 2020, organized
by S. G. Vrachimis, D. G. Eliades, R. Taormina, Z. Kapelan, A. Ostfeld, S. Liu, M. Kyriakou,
P. Pavlou, M. Qiu, and M. M. Polycarpou, as part of the 2nd International CCWI/WDSA
Joint Conference in Beijing, China, aims at objectively comparing the performance of methods
for the detection and localization of leakage events, relying on SCADA measurements of flow and
pressure sensors installed within water distribution networks.

The competition problem was based on L-Town, a small hypothetical town which experiences a large
number of pipe breaks and water losses, affecting its service quality. The L-Town EPANET model and
the SCADA measurements provided were generated based on a real water distribution network in a city
in Cyprus. Participants have been invited to use different tools and methods to detect and localize
the leakage events that occurred in L-Town in 2019, given the availability of a historical SCADA
dataset of the year 2018 and the evaluation SCADA dataset of the year 2019.
The teams, without knowing the solution to the problem, have submitted a results file indicating
the location and time of the detected leakages.

## How to Use

- `2018 SCADA.xlsx` historical dataset (also in CSV): The historical data have been collected for
the period 2018-01-01 00:00 until 2018-12-31 23:55, at 5-minute time steps. The SCADA dataset is
comprised of the water tank level, the flow sensors, the AMR measurements and the pressure sensors.
- `2018 Leak Report.txt` (TXT): The repair times of pipe bursts that have been fixed are provided.
- `L-Town.inp` EPANET Model (INP): A model of the network is provided with nominal parameters for
all the system elements. The nominal base demands for each node are based on average historical
metered consumption. In general, the difference between the actual and the nominal values for each
consumer type (residential and commercial) is less than 10%. Weekly demand profiles for two consumer
types (residential and commercial) are also provided, however they do not capture the
yearly seasonality. Furthermore, the EPANET model parameters may be different from the actual
network parameters (e.g., diameters, roughness coefficients), and it is assumed than in general this
difference is no greater than 10% of the nominal values.
- `2019 SCADA.xlsx` evaluation Dataset (also in CSV): The evaluation data have been collected for
the period 2019-01-01 00:00 until 2019-12-31 23:55, at 5-minute time steps. The SCADA dataset is
comprised of the water tank level, the flow sensors, the AMR measurements and the pressure sensors.
This dataset was used for the evaluation of the competing leakage detection methodologies,
and was disclosed in January 2020.

### Usage in Python

This benchmark is also available in Python under the key "*KIOS-BattLeDIM*":
```python
battledim = load("KIOS-BattLeDIM")
```

Detailed information about the provided functionality can be found in the
[documentation](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.battledim.html).

## Reference

S. G. Vrachimis, D. G. Eliades, R. Taormina, Z. Kapelan, A. Ostfeld, S. Liu, M. Kyriakou, P. Pavlou,
M. Qiu, and M. M. Polycarpou. Forthcoming. *Battle of the Leakage Detection and Isolation Methods*,
Journal of Water Resources Planning and Management, 10.1061/(ASCE)WR.1943-5452.0001601