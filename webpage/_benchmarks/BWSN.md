---
title: "The Battle of the Water Sensor Networks (BWSN)"
id: "bwsn"
permalink: /benchmarks/BWSN.html
collection: benchmarks
layout: benchmark
---

## Description

Following the events of September 11, 2001, in the United States, world public awareness for
possible terrorist attacks on water supply systems has increased dramatically. Among the different
threats for a water distribution system, the most difficult to address is a deliberate chemical
or biological contaminant injection, due to both the uncertainty of the type of
injected contaminant and its consequences, and the uncertainty of the time and location of
the injection. An online contaminant monitoring system is considered as a major opportunity to
protect against the impacts of a deliberate contaminant intrusion. However, although optimization
models and solution algorithms have been developed for locating sensors, little is known about how
these design algorithms compare to the efforts of human designers, and thus, the advantages they
propose for practical design of sensor networks. To explore these issues, the
Battle of the Water Sensor Networks (BWSN) was undertaken as part of the
8th Annual Water Distribution Systems Analysis Symposium, Cincinnati, Ohio, August 27–29, 2006.

Participants were asked to provide designs for locating five sensors and 20 sensors for a
base case (A) and three derivative cases (B), (C), and (D). In this context, two new
water distribution networks, [BWSN-1](network-BWSN-1.html) and [BWSN-2](network-BWSN-2.html),
were introduced. Participants had to provide sensor placements for both networks.

#### Base Case A
1. All quantities affecting network model water quality predictions were assumed to be known and
deterministic. Sensor network designs were challenged by an ensemble of contamination scenarios
sampled from a statistical distribution; the probability distribution of contamination events is
described herein. Contaminant intrusions occurred at network nodes, with an injection flow rate of
125 L/h, contaminant concentration of 230,000 mg/L, and injection duration of 2 h.
The contaminant was assumed conservative after injection. Each contamination scenario involved a
single injection location, which may occur at any network node and begin at any time with equal
probability. For purposes of design evaluation, contaminant concentrations were evaluated using
a 5-min time step.
2. For purposes of calculating the expected population affected
prior to detection (Z_2): phi = 2 L/day, beta = 0.34 (-), D_50 = 41 mg/kg, and W = 70 kg.
For purposes of estimating node population, the total per capita water demand rate was assumed
to be 300 L/day.
3. For purposes of calculating the expected demand of contaminated water prior to detection (Z_3),
the hazard concentration threshold was C = 0.3 mg/L.
4. Sensors instantly detected any nonzero contaminant concentration and action was taken to
eliminate further exposure without delay.

#### Derivative Case B
Identical to Base Case A except that the injection duration was increased to 10 h.

#### Derivative Case C
Identical to Base Case A except that the response delay was 3 h, i.e., it took 3 h after detection
for emergency response to limit contaminant exposure.

#### Derivative Case D
Identical to Base Case A except that all contamination scenarios involved two injection locations,
which may occur at any two distinct nodes with equal probability. The contamination scenario may
begin at any time with equal probability, but both injections were synchronized to begin at
the same time.


## Reference

Avi Ostfeld, James G. Uber, Elad Salomons, Jonathan W. Berry, William E. Hart, Cindy A. Phillips,
Jean-Paul Watson, Gianluca Dorini, Philip Jonkergouw, Zoran Kapelan, Francesco di Pierro,
Soon-Thiam Khu, Dragan Savic, Demetrios Eliades, Marios Polycarpou, Santosh R. Ghimire,
Brian D. Barkdoll, Roberto Gueli, Jinhui J. Huang, Edward A. McBean, William James, Andreas Krause,
Jure Leskovec, Shannon Isovitsch, Jianhua Xu, Carlos Guestrin, Jeanne VanBriesen, Mitchell Small,
Paul Fischbeck, Ami Preis, Marco Propato, Olivier Piller, Gary B. Trachtman, Zheng Yi Wu,
and Tom Walski. (2008).
*The battle of the water sensor networks (BWSN): A design challenge for engineers and algorithms.*
Journal of water resources planning and management, 134(6).
[<i class="bi bi-link"></i>](https://doi.org/10.1061/(ASCE)0733-9496(2008)134:6(556))