# WaterBenchmarkHub

The *WaterBenchmarkHub* is a platform for providing benchmark resources regarding Water Distribution Networks (WDNs).

## Installation

WaterBenchmarkHub supports Python 3.9 - 3.12

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
    # Load GECCO water quality benchmark
    benchmark = load("GeccoWaterQuality")

    # Load 2019 data set
    data = benchmark.load_gecco2019_water_quality_data(return_X_y=True)

    # Show number of samples
    X_train, y_train = data["train"]
    X_val, y_val = data["validation"]
    X_test, y_test = data["test"]
    print(X_train.shape, X_val.shape, X_test.shape)
```

## Documentation

Documentation is available on readthedocs:
[https://water-benchmark-hub.readthedocs.io/en/latest/](https://water-benchmark-hub.readthedocs.io/en/latest/)

## License

MIT license -- see [LICENSE](LICENSE)

## How to Cite?

If you use this software, please cite it as follows:

```
@misc{github:water_benchmark_hub,
        author = {André Artelt},
        title = {WaterBenchmarkHub},
        year = {2024},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{https://github.com/WaterFutures/WaterBenchmarkHub}}
    }
```

## How to Contribute?

Contributions (e.g. creating issues, pull-requests, etc.) are welcome -- please make sure to read the
[code of conduct](CODE_OF_CONDUCT.md) and follow the [developers' guidelines](DEVELOPERS.md).
