---
title: "Battle of the Water Calibration Networks (BWCN)"
id: "bwcn"
permalink: /benchmarks/BWCN.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of the Water Calibration Networks (BWCN) is the third in a series of "Battle
Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.

The competition is about calibrated hydraulic simulation model of the
[C-Town network](network-CTown.html) and was held as part of the 12th Water Distribution
Systems Analysis conference in Tucson, Arizona, in September 2010.

Calibration is a process of comparing model results with field data and making the appropriate
adjustments so that both results agree. Calibration methods can involve formal optimization methods
or manual methods in which the modeler informally examines alternative model parameters.
The development of a calibration framework typically involves the following:

1. definition of the model variables, coefficients, and equations
2. selection of an objective function to measure the quality of the calibration
3. selection of the set of data to be used for the calibration process
4. selection of an optimization/manual scheme for altering the coefficient values in the direction
of reducing the objective function.

Hydraulic calibration usually involves the modification of system demands, fine-tuning the
roughness values of pipes, altering pump operation characteristics, and adjusting other
model attributes that affect simulation results, in particular those that have significant
uncertainty associated with their values. From the previous steps, it is clear that
model calibration is neither unique nor a straightforward technical task. The success of a
calibration process depends on the modeler’s experience and intuition, as well as on the
mathematical model and procedures adopted for the calibration process.


## Reference

Avi Ostfeld, Elad Salomons, Lindell Ormsbee, James G. Uber, Christopher M. Bros, Paul Kalungi,
Richard Burd, Boguslawa Zazula-Coetzee, Teddy Belrain, Doosun Kang, Kevin Lansey, Hailiang Shen,
Edward McBean, Zheng Yi Wu, Tom Walski, Stefano Alvisi, Marco Franchini, Joshua P. Johnson,
Santosh R. Ghimire, Brian D. Barkdoll, Tiit Koppel, Anatoli Vassiljev, Joong Hoon Kim,
Gunhui Chung, Do Guen Yoo, Kegong Diao, Yuwen Zhou, Ji Li, Zilong Liu, Kui Chang, Jinliang Gao,
Shaojian Qu, Yixing Yuan, T. Devi Prasad, Daniele Laucelli, Lydia S. Vamvakeridou Lyroudia,
Zoran Kapelan, Dragan Savic, Luigi Berardi, Giuseppe Barbaro, Orazio Giustolisi, Masoud Asadzadeh,
Bryan A. Tolson, and Robert McKillop (2012).
*Battle of the water calibration networks.* Journal of water resources planning and management,
138(5).