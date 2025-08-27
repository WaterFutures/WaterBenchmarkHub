---
title: "DiTEC-WDN: A Large-Scale Dataset of Hydraulic Scenarios across Multiple Water Distribution Networks"
id: "ditec"
permalink: /benchmarks/DiTEC.html
collection: benchmarks
layout: benchmark
---


## Description

DiTEC-WDN is a simulated dataset consisting of 36,000 unique scenarios simulated on 36 publicly available WDN (1,000 scenarios per network). The goal is to provide a dataset for scenario analysis and study comparisons.

The parameters measured include pressure, flow rate and demand patterns. The dataset contains 10 WDN with short-term (24 hours) scenarios and 26 WDN with long-term (1 year) scenarios, both with a time step of 1 hour.

The generated demand comprises 3 components: a daily pattern, a yearly seasonal pattern and white noise, which are multiplied with each node's base demand.

The dataset is introduced by Truong, H., Tello, A., Lazovik, A. and Degeler, V.

## How to Use

The simulation source code is available on [Github](https://github.com/DiTEC-project/DiTEC_WDN_dataset) and the simulated data on [Hugging Face](https://huggingface.co/datasets/rugds/ditec-wdn).

## Reference

Huy Truong and Andrés Tello and Alexander Lazovik and Victoria Degeler (2025).
*DiTEC-WDN: A Large-Scale Dataset of Hydraulic Scenarios across Multiple Water Distribution Networks*
Submitted to Nature Scientific Data
[<i class="bi bi-link"></i>](https://doi.org/10.48550/arXiv.2503.17167)