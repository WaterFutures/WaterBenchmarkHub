---
title: "WDSEventDB (Water Distribution System Event Database)" 
id: "wdseventdb"
permalink: /benchmarks/WDSEventDB.html
collection: benchmarks
layout: benchmark  
---

## Description
The `WDSEventDB` benchmark is an open-source, real-time dataset collected from a sensor-instrumented water distribution testbed, featuring cyberattack, leakage, and sensor-failure events for event diagnosis and anomaly detection research.

## How to Use 
The dataset contains measurements collected from a physical WDS testbed under four operating conditions: 
1. **Clean** — fault-free baseline data (``CleanData.xlsx``).
2. **Cyberattack** — one combined cyber-event file covering events 1-4 (``CyberEvent1-4.xlsx``).
3. **Leakage** — three individual leakage event files(``LeakEvent1 - 3.xlsx``).
4. **Sensor Failure** — four sensor-failure event files covering sensor pairs 1, 2-3, 4-5, and 6-7 (``SensorEvent1.xlsx``, ``SensorEvent23.xlsx``, ``SensorEvent45.xlsx``, ``SensorEvent67.xlsx``).

### Usage in Python
This benchmark is also available in Python under the key "*WDSEventDB*": 
```python
wdseventdb = load("WDSEventDB")
```

The entire data set can be loaded using the
[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.wds_eventdb.html#module-water_benchmark_hub.wds_eventdb.wds_eventdb.InTaSet.load_data)
function.

## Reference
Raza, N., Iwakin, O., Daniela, V., Putri, S. A., & Moazeni, F. (2025). WDSEventDB: A Real-Time Benchmark Dataset for Event Diagnosis in Water Distribution Networks  
[<i class="bi bi-link"></i>](https://doi.org/10.5281/zenodo.17547955)