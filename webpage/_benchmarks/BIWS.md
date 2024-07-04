---
title: "Battle of the Intermittent Water Supply (BIWS)"
id: "biws"
permalink: /benchmarks/BIWS.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of Intermittent Water Supply (BIWS) is the 9th in the series of
"Battle Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.
It took place during the 2nd International Joint Conference on Water Distribution System Analysis
(WDSA) and Computing and Control in the Water Industry (CCWI), held in Valencia (Spain) in
July 2022 at the Polytechnic University of Valencia (Valencia Tech).

Participants had to find the best solution to reverse the situation of the BIWS network
(also refered to as the E-Town network) from intermittent supply to continuous 24x7 supply with
enough pressure. The current state and mode of operation of a given pilot network was the
starting point of the battle. Leaks are assumed pinpointed and were provided as starting data.
The demand is satisfied through household roof tanks or ground level tanks, which data was given
as well. Besides, the total quantity of water available is limited.

Although recovering normal supply conditions is a complex problem, the battle focused on improving
the network infrastructure. It is assumed that the manager has a certain amount of money to invest
annually, for a period of five years. A series of possible actions to take are declared, each with
an associated cost and a degree of achievement of the objectives.

## How to Use

- [`BIWS.inp`](https://wdsa-ccwi2022.upv.es/wp-content/uploads/descargas/BIWS.inp):
EPANET file with the current network status.
- [`Leakages.xlsx`](https://wdsa-ccwi2022.upv.es/wp-content/uploads/descargas/Leakages.xlsx):
Contains all leaky pipes together with their position and emitter coefficient
(for modeling the leak demand) -- note that the leaks (i.e. emitter coefficients) are supposed
to grow over time (weekly steps).

## Reference

Pedro L. Iglesias-Rey, Fernando Martínez-Alzamora, F. Javier Martínez Solano, Avi Ostfeld, (2022).
*Battle of Intermittent Water Supply (BIWS).*
2nd International Joint Conference on Water Distribution System Analysis (WDSA) and Computing and
Control in the Water Industry (CCWI)