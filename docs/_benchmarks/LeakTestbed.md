---
title: "LeakTestbed: Dataset of Leak Simulations in Experimental Testbed Water Distribution System"
id: "leaktestbed"
permalink: /benchmarks/LeakTestbed.html
collection: benchmarks
layout: benchmark
---


## Description

This is the first fully labeled open dataset for leak detection and localization in
water distribution systems. This dataset includes two hundred and eighty signals acquired
from a laboratory-scale water distribution testbed with four types of induced leaks and no-leak.
The testbed was 47 m long built from 152.4 mm diameter PVC pipes. Two accelerometers (A1 and A2),
two hydrophones (H1 and H2), and two dynamic pressure sensors (P1 and P2) were deployed to measure
acceleration, acoustic, and dynamic pressure data. The data were recorded through controlled
experiments where the following were changed: network architecture, leak type,
background flow condition, background noise condition, and sensor types and locations.
Each signal was recorded for 30 seconds. Network architectures were looped (LO) and branched (BR).
Leak types were Longitudinal Crack (LC), Circumferential Crack (CC), Gasket Leak (GL),
Orifice Leak (OL), and No-leak (NL).
Background flow conditions included 0 L/s (ND), 0.18 L/s, 0.47 L/s, and Transient
(background flow rate abruptly changed from 0.47 L/s to 0 L/s at the second 20th of 30-second
long measurements). Background noise conditions, with noise (N) and without noise (NN), determined
whether a background noise was present during acoustic data measurements. 

## How to Use

[Accelerometer](https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/30110f76-4804-4512-bca5-46b8e67dffaf/file_downloaded)
and [dynamic pressure data](https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/3a8b5e09-0586-4f88-8202-337a53adc98c/file_downloaded)
are in ‘.csv’ format, and the
[hydrophone data](https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/db8d1475-7cb4-4c60-b9e2-7d47a7d95971/file_downloaded)
are in ‘.raw’ format with 8000 Hz frequency.
The file [Python code to convert raw acoustic data to pandas DataFrame.py](https://data.mendeley.com/public-files/datasets/tbrnp6vrnj/files/dc9d459b-ec6d-4a64-ab69-d2bac7396a5c/file_downloaded) converts the
raw hydrophone data to DataFrame in Python. 


## Reference

Mohsen Aghashahi, Lina Sela, M. Katherine Banks (2022).
*Benchmarking dataset for leak detection and localization in water distribution systems.*
In: Data in Brief
[<i class="bi bi-link"></i>](https://doi.org/10.1016/j.dib.2023.109148)