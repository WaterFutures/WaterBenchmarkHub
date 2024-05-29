.. _basic_usage:

***********
Basic Usage
***********

Quick example
-------------

.. code-block:: python

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