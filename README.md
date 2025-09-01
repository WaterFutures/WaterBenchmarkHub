# WaterBenchmarkHub
[![pypi](https://img.shields.io/pypi/v/water-benchmark-hub.svg)](https://pypi.org/project/water-benchmark-hub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/water-benchmark-hub)
[![Documentation Status](https://readthedocs.org/projects/waterbenchmarkhub/badge/?version=stable)](https://waterbenchmarkhub.readthedocs.io/en/stable/?badge=stable)
[![Downloads](https://static.pepy.tech/badge/water-benchmark-hub)](https://pepy.tech/project/water-benchmark-hub)
[![Downloads](https://static.pepy.tech/badge/water-benchmark-hub/month)](https://pepy.tech/project/water-benchmark-hub)

The [*WaterBenchmarkHub*](https://waterfutures.github.io/WaterBenchmarkHub) is a platform for
accessing and sharing Water Distribution Network (WDN) benchmarks and data sets.
The webpage is available at
[https://waterfutures.github.io/WaterBenchmarkHub](https://waterfutures.github.io/WaterBenchmarkHub)
-- see [docs/](docs/) for details such as source code, etc.

The availability and accessibility of benchmarks are essential for reproducible research as well as
for accelerating scientific progress.
A benchmark is a *verified* data set or resource (e.g. a water distribution network) together with an
evaluation functions that can evaluate different algorithms/methods under the same criteria.

The WaterBenchmarkHub is also available as a Python package *water-benchmark-hub*.

## Call for Contributions

If you have a benchmark (resource) that is not yet available in the *WaterBenchmarkHub*,
please either create a new issue or read on
[How to Contribute](https://waterbenchmarkhub.readthedocs.io/en/latest/how_to_contribute.html).

## Installation of the Python Package

The Python package supports Python 3.9 - 3.13

### PyPI

```
pip install water-benchmark-hub
```

### Git
Download or clone the repository:
```
git clone https://github.com/WaterFutures/WaterBenchmarkHub.git
cd WaterBenchmarkHub
```

Install all requirements as listed in [REQUIREMENTS.txt](REQUIREMENTS.txt):
```
pip install -r REQUIREMENTS.txt
```

Install the benchmark hub:
```
pip install .
```

## Quick Example

```python
from water_benchmark_hub import load


if __name__ == "__main__":
    # Load the GECCO Water Quality 2019 benchmark
    benchmark = load("GECCO-WaterQuality2019")

    # Load data set
    data = benchmark.load_data(return_X_y=True)

    # Show number of samples
    X_train, y_train = data["train"]
    X_val, y_val = data["validation"]
    X_test, y_test = data["test"]
    print(X_train.shape, X_val.shape, X_test.shape)
```

## Documentation

Documentation is available on readthedocs:
[https://waterbenchmarkhub.readthedocs.io/en/stable/](https://waterbenchmarkhub.readthedocs.io/en/stable/)

## License

MIT license -- see [LICENSE](LICENSE)

## How to Cite?

If you use the WaterBenchmarkHub in your research, please cite it as follows:

```
@article{Artelt_Giese_Vrachimis_Eliades_Polycarpou_Hammer_2025,
    title={{The WaterBenchmarkHub: A Platform for Benchmarks in Water Distribution Networks}},
    DOI={10.15131/SHEF.DATA.29921051.V1},
    journal={21st Computing and Control in the Water Industry Conference (CCWI 2025) at the University of Sheffield (1st - 3rd September 2025)},
    publisher={The University of Sheffield},
    author={Artelt, André and Giese, Katharina and Vrachimis, Stelios G. and Eliades, Demetris G. and Polycarpou, Marios M. and Hammer, Barbara},
    year={2025},
    url = {https://github.com/WaterFutures/WaterBenchmarkHub}
}
```

## How to get Support?

If you come across any bug or need assistance please feel free to open a new issue if none of the existing issues answers your questions.

## How to Contribute?

Contributions (e.g. creating issues, pull-requests, etc.) are welcome -- please make sure to read
[How to Contribute](https://waterbenchmarkhub.readthedocs.io/en/latest/how_to_contribute.html),
the [code of conduct](CODE_OF_CONDUCT.md) and follow the [developers' guidelines](DEVELOPERS.md).
