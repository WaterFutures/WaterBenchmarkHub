---
title: "{full_name}"
id: "{network_id_lower}"
permalink: /benchmarks/network-{name}.html
collection: benchmarks
layout: benchmark
---

## Description

{long_description}

{networks_architecture_description}

{image_link}

## How to Use

The {name} network is provided as an .inp file and can be loaded into EPANET or any other software package
supporting .inp files.

### Usage in Python

The {name} network is also available in Python through the key "*{network_id}*":
```python
network = load("{network_id}")
{name_lower}_inp = network.load()
```

Detailed information about the provided functionality can be found in the documentation of
[`load()`](https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.{name}.load).


## Reference

{references}
