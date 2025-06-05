---
title: "A Benchmark for Physics-informed Machine Learning of Chlorine Concentration States in Water Distribution Networks"
id: "clstateestimate"
permalink: /benchmarks/ClStateEstimate.html
collection: benchmarks
layout: benchmark
---

## Description

Ensuring high-quality drinking water is a critical responsibility of water utilities, with chlorine being the main disinfectant typically used. Accurate estimation of chlorine concentrations in the dynamic environment of water distribution networks (WDNs) is essential to ensure safe water supply. This benchmark constitutes a comprehensive and carefully created benchmark for training and evaluation of chlorine concentration estimation methodologies in WDNs. The benchmark includes a diverse dataset of 18,000 scenarios of the widely studied [Hanoi](network-Hanoi.html), [Net1](network-Net1.html), and the more recent and complex [CY-DBP](network-CY-DBP.html) water networks, featuring various chlorine injection patterns to capture diverse physical dynamics. In addition to the data, the benchmark also provides baselines in the form of two neural surrogate models for chlorine state estimation: a physics-informed Graph Neural Network (GNN) and a physics-guided Recurrent Neural Network (RNN).


## Reference

L. Hermes, A. Artelt, S. G. Vrachimis, M. M. Polycarpou, and B. Hammer (2025). *A Benchmark for Physics-informed Machine Learning of Chlorine States in Water Distribution Networks*,
SN Computer Science
[<i class="bi bi-link"></i>](https://doi.org/10.1007/s42979-025-04008-y)