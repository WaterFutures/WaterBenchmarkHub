---
title: "BATADAL (BATtle of the Attack Detection ALgorithms)"
id: "batadal"
permalink: /benchmarks/BATADAL.html
collection: benchmarks
layout: benchmark
---

## Description

The BATtle of the Attack Detection ALgorithms (*BATADAL*) is the 7th in a series of "Battle
Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.
It is a competition on planning and management of water networks undertaken within the Water
Distribution Systems Analysis Symposium. The goal of the battle was to compare the performance
of algorithms for the detection of cyber-physical attacks, whose frequency has increased in
the last few years along with the adoption of smart water technologies. The design challenge was
set for the [C-Town network](network-CTown.html), a real-world, medium-sized water distribution
system operated through programmable logic controllers and a supervisory control and
data acquisition (SCADA) system. Participants were provided with data sets containing (simulated)
SCADA observations, and challenged to design an attack detection algorithm.
The effectiveness of all submitted algorithms was evaluated in terms of time-to-detection and
classification accuracy. Seven teams participated in the battle and proposed a variety of
successful approaches leveraging data analysis, model-based detection mechanisms, and rule checking.
Results were presented at the Water Distribution Systems Analysis Symposium
(World Environmental and Water Resources Congress) in Sacramento, California on May 21-25, 2017.

## How to Use

- **Training Dataset 1:** [`BATADAL_dataset03.csv`](https://www.batadal.net/data/BATADAL_dataset03.csv):
This dataset was released on November 20 2016, and it was generated from a one-year long simulation.
The dataset does not contain any attacks, i.e. all the data pertains to C-Town normal operations.
- **Training Dataset 2:** [`BATADAL_dataset04.csv`](https://www.batadal.net/data/BATADAL_dataset04.csv):
This dataset with partially labeled data was released on November 28 2016. The dataset is around
6 months long and contains several attacks, some of which are approximately labeled.
- **Test Dataset:** `BATADAL_test_dataset.csv` (in [`BATADAL_test_dataset.zip`](https://www.batadal.net/data/BATADAL_test_dataset.zip)):
This 3-months long dataset contains several attacks but no labels. The dataset was released on
February 20 2017, and it is used to compare the performance of the algorithms
(see competition rules document for details).

The column `ATT_FLAG` contains the label indicating the presence of an attack --
i.e. "1" if an attack is present.
The other 43 columns contain the sensor readings (such as water level in tanks,
pressure at junctions, pump and valve states, etc.) that have to be used to predict the presenence
of an attack -- note that those sensor readings might have been manipulated by an attacker.

### Usage in Python

This benchmark is also available in Python under the key "*BATADAL*":
```python
batadal = load("BATADAL")
```

Detailed information about the provided functionality can be found in the
[documentation](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.batadal.html).

## Reference

Taormina, R., Galelli, S., Tippenhauer, N. O., Salomons, E., Ostfeld, A., Eliades, D. G., ... &
Ohar, Z. (2018).
*Battle of the attack detection algorithms: Disclosing cyber attacks on water distribution networks.*
Journal of Water Resources Planning and Management, 144(8), 04018048.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969)