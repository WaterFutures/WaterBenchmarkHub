---
title: "Leakage Repairs Dataset" 
id: "kios-leakagerepairs"
permalink: /benchmarks/KIOS-LeakageRepairs.html
collection: benchmarks
layout: benchmark  
---

## Description
The `KIOS Leakage Repairs Dataset` is a real-world benchmark dataset from a Cyprus water distribution network that pairs 5-minute DMA inlet flow time series with verified leakage repair logs (processed, severity-classified, and temporally aligned) to provide ground-truth labels for leakage detection and localization under operational conditions.

## How to Use
The dataset contains real-world data collected from a water distribution network in Cyprus, covering:
1. **Leak reports**: field repair reports (``leak_reports.csv``) with columns: ``topic`` (Greek-language event category), ``reason``, ``action``, ``area`` (``Area_1`` - ``Area_6``), ``timestamp``, ``severity`` (``Low`` / ``Med`` / ``High``), and ``repeated`` (integer repair count).
2. **Flow measurements** — raw time-series flow data for each of the six monitored areas (``Area_1.csv`` - ``Area_6.csv``) with columns: ``result_time`` and ``Flow``.

### Usage in Python
This benchmark is also available in Python under the key "*KIOS-LeakageRepairs*": 
```python
leakage_repairs = load("KIOS-LeakageRepairs")
```

Detailed information about the provided functionality can be found in the

[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.leakage_repairs.html#module-water_benchmark_hub.leakage_repairs.leakage_repairs) function.

## Reference

