---
title: "Multisource WDN Anomaly " 
id: "multisource-wdn-anomaly"
permalink: /benchmarks/multisource-wdn-anomaly.html
collection: benchmarks
layout: benchmark  
---

## Description
The `Multisource WDN Anomaly` benchmark provides hourly anomaly scores and leak labels from an anonymized urban water distribution network (WDN). It combines three data sources: SCADA sensor readings from water sources, operational energy usage of pumping stations, and environmental conditions (temperature, groundwater level). Anomaly scores were generated with Elastic ML and Isolation Forest. The binary label marks hours within ±7 days of a real leak event recorded in the utility's PTIS system. The benchmark supports anomaly detection and leak/fault prediction on real-world data.



## How to Use
The dataset is a single CSV file with one row per hour. Each row has a `timestamp` (format `DD-MM-YYYY HH:MM`), the label `fault_d7`, and 18 anomaly-score columns

### Usage in Python
This benchmark is also available in Python under the key "*MultiSourceWDNAnomaly*": 
```python
multisource_wdn_anomaly = load("MultiSourceWDNAnomaly")
```



The entire data set can be loaded using the
[```load_data()```](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.multisource_wdn_anomaly.html#water_benchmark_hub.multisource_wdn_anomaly.multisource_wdn_anomaly.MultiSourceWDNAnomaly.load_data)
function.


## Reference
Jan, B., Munk, M., & Munkova, D. (2025). Hourly Anomaly Scores and Leak Labels from a Multi-Source Urban Water Distribution Network Dataset. 
[<i class="bi bi-link"></i>](https://doi.org/10.5281/zenodo.15096167)
