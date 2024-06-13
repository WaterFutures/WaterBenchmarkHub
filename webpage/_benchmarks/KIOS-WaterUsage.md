---
title: "Water-Usage-Dataset"
id: "kios-waterusage"
permalink: /benchmarks/KIOS-WaterUsage.html
collection: benchmarks
layout: benchmark
---

## Description

This dataset concerns the monitoring of water usage of different household appliances. Informing consumers about it has been shown to have an impact on their behavior toward drinking water conservation. The data were created using the STochastic Residential water End-use Model (STREaM) [[Cominola et al., 2018](https://scholarsarchive.byu.edu/iemssconference/2016/Stream-C/46/)], a modeling software developed that generates synthetic time series data of a household.

Some statistics about the data set:

- **Resolution:** 10s
- **Number of Appliances:** 5
- **Active Appliances:** standard toilet, standard shower, standard faucet, high-efficiency clothes washer and standard dishwasher
- **Household:** 2-person
- **Dataset Duration:** Training dataset - 90 days, Validation dataset - 45 days, Testing dataset - 45 days


## How to Use

- **Train Files:**
`Trainset.csv`: CSV file containing the 6 columns of data. The total consuption and 5 columns indicating the consumption of the appliance/s that is/are active.
- **Validation Files:**
`Validationset.csv`: CSV file containing the 6 columns of data. The total consuption and 5 columns indicating the consumption of the appliance/s that is/are active.
- **Test Files:**
`Testset.csv`: CSV file containing the 6 columns of data. The total consuption and 5 columns indicating the consumption of the appliance/s that is/are active.

### Usage in Python

This benchmark is also available in Python under the key "*KIOS-WaterUsage*":
```python
water_usage = load("KIOS-WaterUsage")
```

The entire data set (i.e. train, validation, and test data) can be loaded using the [```load_data()```](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.water_usage.html#water_benchmark_hub.water_usage.water_usage.WaterUsage.load_data) function.

Besides the data set, this benchmark also provides the original evaluation function implemented in [```compute_evaluation_score()```](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.water_usage.html#water_benchmark_hub.water_usage.water_usage.WaterUsage.compute_evaluation_score) which computes the accuracy, precision, F1-score, Cohen's kappa, and ROC AUC.

Detailed information about the provided functionality can be found in the
[documentation](https://water-benchmark-hub.readthedocs.io/en/stable/water_benchmark_hub.water_usage.html).

## Reference

P. Pavlou, S. Filippou, S. Solonos, S. G. Vrachimis, K. Malialis, D. G. Eliades, T. Theocharides, M. M. Polycarpou. *Monitoring domestic water consumption: A comparative study of model-based and data-driven end-use disaggregation methods.* Journal of Hydroinformatics.