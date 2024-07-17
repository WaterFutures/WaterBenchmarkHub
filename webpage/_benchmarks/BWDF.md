---
title: "Battle of Water Demand Forecasting (BWDF)"
id: "bwdf"
permalink: /benchmarks/BWDF.html
collection: benchmarks
layout: benchmark
---

## Description

The Battle of Water Demand Forecasting (BWDF) is the 10th in the series of
"Battle Competitions" dating back to the Battle of the Water Networks (BWN) in 1985.
It took place during the 3nd International Joint Conference on Water Distribution System Analysis
(WDSA) and Computing and Control in the Water Industry (CCWI), held in Ferrara, Italy in July 2024.

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

## How to Use

- [`Inflow_Data_4.xlsx`](https://wdsa-ccwi2024.it/wp-content/uploads/2024/03/Inflow_Data_4.xlsx):
All inflows (L/s) over time (at a sampling rate of 1h) at the DMAs.
Participants had to provide fours forecasts during the competition: weeks 30/2022, 44/2022, 3/2023,
and 10/2023 based on the data BEFORE that weeks. 
- [`Weather_Data_4.xlsx`](https://wdsa-ccwi2024.it/wp-content/uploads/2024/03/Weather_Data_4.xlsx):
The weather -- i.e. rainfall depth (mm), air temperature (°C), air humidity (%), and
windspeed (km/h) -- over time in the unknown city where the DMAs are located. This data is supposed
to help forecasting the demands.

## Reference

S. Alvisi, M. Franchini, V. Marsili, F. Mazzoni, E. Salomons (2024).
*Battle of Water Demand Forecasting (BWDF).*
3nd International Joint Conference on Water Distribution System Analysis (WDSA) and Computing and
Control in the Water Industry (CCWI)