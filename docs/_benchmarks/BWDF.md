---
title: "Battle of Water Demand Forecasting (BWDF)"
id: "bwdf"
permalink: /benchmarks/BWDF.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of Water Demand Forecasting (BWDF), organized by S. Alvisi, M. Franchini, V. Marsili, F. Mazzoni, and E. Salomons, is the 10th in the series of "Battle of the Water Networks" competitions dating back to the original BWN in 1985 (Walski et al., 1987).
It took place during the 3rd International Joint Conference on Water Distribution System Analysis (WDSA) and Computing and Control in the Water Industry (CCWI), held in Ferrara, Italy in July 2024.

Population growth, urbanization, and climate change have been raising people’s awareness about the
impact of human activities on the environment and the available natural sources, such as
water resource. In this context, a sustainable management of water systems is crucial to avoid water
shortage or the depletion of the available sources, and the operational and strategic decisions made
by drinking water utilities can take benefit from a reliable and accurate forecast of water demand,
which is the main driver of water distribution systems (WDSs).

The competition aims at comparing the effectiveness of methods for the short-term forecast of
urban water demand in a set of real District Metered Areas (DMAs) belonging to an unknown city in
northern Italy. The water-demand forecasting problem can be solved by applying different types of
methods and approaches, including -- but not limited to -- engineering judgement, probabilistic
and statistical methods, machine learning tools, and signal-processing models.

For more information, see [Alvisi et al. (2025)](https://ascelibrary.org/doi/10.1061/JWRMD5.WRENG-6887).

This module provides functions for loading the original competition dataset, the complete dataset released as supplementary material to the publication, and for testing your forecasts using the same specifications as the original competition.

Note:
This module exposes only the core functionalities of the more extended package `wf4bwdf`. To access additional features and utilities, please install the extended package:

```bash
pip install wf4bwdf
```

For more details, visit the [wf4bwdf documentation or repository](https://github.com/WaterFutures/wf4bwdf).

## Core Functions

- `load_complete_dataset`: Load the full supplementary dataset (DMA inflows, weather, calendar, metadata).
- `load_iteration_dataset`: Load the original competition dataset for a specific evaluation week.
- `evaluate`: Evaluate your forecast using the official competition metrics.

## How to Use

### 1. Load complete dataset

Make sure that you have installed the the optinal `bwdf` dependencies by running

```bash
pip install water-benchmark-hub[bwdf]
```

The function `load_complete_dataset` provides access to **DMA inflows and weather data** from the supplementary information of Alvisi et al. (2025), as well as calendar information and other problem metadata in machine-readable format.

```python
from water_benchmark_hub.bwdf import BWDF as bwdf

dataset = bwdf.load_complete_dataset()

# Print DMA description
print(dataset['dma-properties']['Description'])

# Plot DMA 3(C) inflow
dma_c_inflow = dataset['dma-inflows']['DMA 3']
# plot the series
```

### 2. Load original dataset and evaluate forecasts following the competition requirements
The `evaluate` function works only if the forecast is a complete prediction of one of the original evaluation weeks and for at least one DMA.
```python
from water_benchmark_hub.bwdf import BWDF as bwdf
import pandas as pd

for iteration in range(1,5):
    # Load the data for that iteration (no leak of future information) using letters instead of the numbers (e.g., 'DMA C')
    dataset = bwdf.load_iteration_dataset(iteration, use_letters_for_names=True)

    # Compute your forecast: previous week
    forecast = dataset['dma-inflows'].iloc[-168:]
    forecast.index = forecast.index + pd.Timedelta(weeks=1)

    # Evaluate the forecast
    results = bwdf.evaluate(forecast)

    # Should have returned a series with the combination 'Evaluation week', DMA, and BWDF performance indicators')
    print(results)
```

This benchmark is also available in Python under the key "*BWDF*":

```python
bwdf = load("BWDF")
```

Detailed information about the provided functionality can be found in the [documentation](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.bwdf.html).

## Reference

S. Alvisi, M. Franchini, V. Marsili, F. Mazzoni, E. Salomons (2025). *Battle of Water Demand Forecasting*, Journal of Water Resources Planning and Management, vol. 151, no. 10.
[<i class="bi bi-link"></i>](https://doi.org/10.1061/JWRMD5.WRENG-6887)