---
title: "GECCO Industrial Challenge 2017 Dataset"
id: "gecco-waterquality2017"
permalink: /benchmarks/GECCO-WaterQuality2017.html
collection: benchmarks
layout: benchmark
---

## Description

The GECCO Industrial Challenge 2017 Dataset: A water quality dataset for the
"Monitoring of drinking-water quality" competition organized by M. Friese, J. Stork,
A. Fischbach, M. Rebolledo, T. Bartz-Beielstein at the Genetic and Evolutionary
Computation Conference 2017, Berlin, Germany

This is a benchmark for anomaly detection algorithms on water quality. The data is provided by
the "Thüringer Fernwasserversorgung" (Germany) and constitutes a real-world data set. In this
data set, 9 numeric water quality features are given at a sampling rate of 1 min over approx.
3 month. The goal is to predict the presence of an anomaly -- i.e. binary classification.

## How to Use

[`1_gecco2017_water_quality.csv`](https://zenodo.org/records/3884465/files/1_gecco2017_water_quality.csv?download=1) contains the entire data set.

| Column  | Description                                                                                      |
|---------|--------------------------------------------------------------------------------------------------|
| `Time`  | Time of measurement, given in following format: yyyy-mm-dd HH:MM:SS                              |
| `Tp`    | The temperature of the water, given in °C.                                                       |
| `Cl`    | Amount of chlorine dioxide in the water, given in mg/L (MS1).                                    |
| `pH`    | PH value of the water.                                                                           |
| `Redox` | Redox potential, given in mV.                                                                    |
| `Leit`  | Electric conductivity of the water, given in μS/cm.                                              |
| `Trueb` | Turbidity of the water, given in NTU.                                                            |
| `Cl_2`  | Amount of chlorine dioxide in the water, given in mg/L (MS2).                                    |
| `Fm`    | Flow rate at water line1, given in m3/h.                                                         |
| `Fm_2`  | Flow rate at water line2, given in m3/h.                                                         |
| `EVENT` | Marker if this entry should be considered as a remarkable change resp. event, given in boolean.  |

### Usage in Python

This benchmark is also available in Python in the GECCO water quality collection (key: *GECCO-WaterQuality2017*)
through the
[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.gecco_waterquality.html#water_benchmark_hub.gecco_waterquality.gecco_water_quality.GeccoWaterQuality2017.load_data)
function:
```python
# Load GECCO water quality benchmark
benchmark = load("GECCO-WaterQuality2017")

# Load data set
data = benchmark.load_data(return_X_y=True)
```

The official evaluation function is implemented in [```compute_evaluation_score()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.gecco_waterquality.html#water_benchmark_hub.gecco_waterquality.gecco_water_quality.GeccoWaterQuality.compute_evaluation_score).

## Reference

Moritz, S., Friese, M., Stork, J., Rebolledo, M., Fischbach, A., & Bartz-Beielstein, T. (2017).
*GECCO Industrial Challenge 2017 Dataset: A water quality dataset for the 'Monitoring of drinking-water quality'*
competition at the Genetic and Evolutionary Computation Conference 2017, Berlin, Germany.
[<i class="bi bi-link"></i>](https://doi.org/10.5281/zenodo.3884464)