---
title: "InTaSet (Interconnected Tank System Dataset)" 
id: "intaset"
permalink: /benchmarks/InTaSet.html
collection: benchmarks
layout: benchmark  
---

## Description
The `Interconnected Tank System Dataset (InTaSet)` is a comprehensive benchmark dataset for nonlinear system identification and sensor-fault detection, based on real-time measurements from a physical interconnected quadruple-tank testbed operating in both open-loop and closed-loop configurations.


## How to Use
The dataset contains two sub-datasets: 
1. **InTaSet-ID**: system identification data across four configurations (``"2T"``, ``"3T"``, ``"4T-M1"``, ``"4T-M2"``), each providing a training and a testing split. 
2. **InTaSet-FD**: sensor-fault detection data consisting of clean (fault-free) training data and three fault scenarios (sensor fault at Tank 1, Tank 3, and Tank 1 & 3 simultaneously).


### Usage in Python
This benchmark is also available in Python under the key "*InTaSet*": 
```python
intaset = load("InTaSet")
```



The entire data set can be loaded using the
[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.intaset.html#water_benchmark_hub.intaset.intaset.InTaSet.load_data)
function.


## Reference
Putri, S. A., Villacrés, D., Raza, N., Iwakin, O., & Moazeni, F. (2025). InTaSet: A Benchmark Dataset for Data-Driven System Identification and Fault Detection in an Interconnected Water System 
[<i class="bi bi-link"></i>](https://doi.org/10.5281/zenodo.17652851 )
