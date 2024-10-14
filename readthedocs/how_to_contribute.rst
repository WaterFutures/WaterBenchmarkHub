.. _how_to_contribute:

*****************
How to Contribute
*****************

This document describes how researchers/users can contribute their own benchmark (resources)
to the WaterBenchmarkHub.

In order to add a new benchmark (resource), the WaterBenchmarkHub Git repository has to be cloned
and a pull-request with all necessary changes (see next sections) must be submitted.
The pull-requests will be reviewed by the WaterBenchmarkHub team before it gets accepted and
finally integrated into the WaterBenchmarkHub.

General
-------

When adding a new benchmark (resource), there are a few aspects that must be considered:

Naming
++++++

The unique identifier of a new benchmark (resource) must consist of two parts:

1. Category or user/organization
2. Name of the benchmark (resource)

Both parts (lowercase!) are concatenated by a hyphen -- i.e. let's assume we add a network
called `Net2`, then the final name would be `network-net2` (note that we use the category `network`
to denote a network resource).

Meta data
+++++++++

For each benchmark (resource), a new entry (dictionary) in the database
`docs/static/database.json <https://github.com/WaterFutures/WaterBenchmarkHub/blob/dev/docs/static/database.json>`_
must be created with the following content -- if a field is not available,
it should dropped from the database entry:

- :code:`name` Name of the benchmark (resource).
- :code:`desc` Brief description of the benchmark (resource).
- :code:`year` Year in which the benchmark (resource) was published.
- :code:`doi` The doi of the benchmark (resource) or the corresponding publication.
- :code:`license` The license of the benchmark (resource).
- :code:`tags` List of (existing) tags associated with the benchmark (resource) --
  avoid inventing new tags and use existing tags!
- :code:`keywords` Additional keywords associated with the benchmark (resource) --
  these keywords are never displayed but used when the user is searching for benchmark (resources).
- :code:`download_url` External URL where the benchmark (resource) can be downloaded --
  should be direct link to the resource file(s). 
- :code:`external_url` External URL to the project page of the benchmark (resource).
- :code:`permalink` Usually, this is given as `benchmarks/benchmark-ID.html`
  where `benchmark-ID` refers to the unique ID of the benchmark resource.

**Note:** The dictionary key (lowercase!) in the database must be the unique identifier of the benchmark (resource).

A complete example of the `KIOS LeakDB` benchmark is given below:

.. code:: JSON

	"kios-leakdb": {
            "name": "LeakDB",
            "desc": "LeakDB (Leakage Diagnosis Benchmark) is a realistic leakage dataset for water distribution networks.",
            "year": 2018,
            "tags": ["leakage detection", "leakage localization", "leakage", "event detection"],
            "keywords": ["Net1", "Hanoi"],
            "doi": "10.5281/zenodo.1313116",
            "license": "EUPL-1.2",
            "download_url": "https://ucy-my.sharepoint.com/:f:/g/personal/mkiria01_ucy_ac_cy/Eiyah0-TL4dGqt9K4Ln5TN0BRlroASbX35p53bS7or4j5A",
            "external_url": "https://github.com/KIOS-Research/LeakDB",
            "permalink": "benchmarks/KIOS-LeakDB.html"
        }

Description
+++++++++++

The complete description of the benchmark resource must be placed in a Markdown file in the
`docs/_benchmarks <https://github.com/WaterFutures/WaterBenchmarkHub/blob/dev/docs/_benchmarks>`_ folder.
The name of the Markdown file must be the same as specified in the :code:`permalink` field
in the database.

The Markdown file must start with the following header:

.. code:: YAML

	---
	title: "BenchmarkName"
	id: "benchmark-ID"
	permalink: benchmark-permalink
	collection: benchmarks
	layout: benchmark
	---
	
where :code:`BenchmarkName` refers to the name, :code:`benchmark-ID` to the unique ID (see above),
and :code:`benchmark-permalink` to the permalink of the benchmark (resource) as specified in
the database.
All other parts of the header must not be changed!

Regarding the description itself, we do not have any strict rules how to structure
and what to put into the Markdown file.
However, we recommend the following layout:

- :code:`## Description` General (detailed) description of the benchmark (resource).
- :code:`## How to Use` Description of how to load and utilize the benchmark (resource)
- :code:`### Usage in Python` If applicable, a description on how to load the benchmark (resource)
  in Python using the *water-benchmark-hub* Python package.
- :code:`## Reference` Reference (citation) of the benchmark (resource).

Images or other resources are used in the Markdown file, must be placed in the
`static/benchmarks/benchmark-ID/` folder -- where `benchmark-ID` (lower case!) refers to the
benchmark ID as given the :code:`permalink` field.


Python package
--------------

In addition to the previous steps, the benchmark (resource) should made be available
(if possible) in the *water-benchmark-hub* Python package as well.
For this, the following steps are necessary:

1. If the new benchmark (resource) is a network, a new class has to be derived from the
   `WaterDistributionNetwork <https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.networks.html#water_benchmark_hub.networks.networks.WaterDistributionNetwork>`_
   class and put into
   `src/water_benchmark_hub/networks/networks.py <https://github.com/WaterFutures/WaterBenchmarkHub/blob/dev/src/water_benchmark_hub/networks/networks.py>`_
   (if justified, a new .py file can also be created).

   For all other types of benchmark (resources), a new directory should be created and
   the benchmark itself must be implemented by deriving a new class from the
   `BenchmarkResource <https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.html#water_benchmark_hub.benchmark_resource.BenchmarkResource>`_
   class and importing this new class in
   `src/water_benchmark_hub/__init__.py <https://github.com/WaterFutures/WaterBenchmarkHub/blob/dev/src/water_benchmark_hub/__init__.py>`_.
2. In all cases, the new benchmark (resource) must be registered by calling the
   `register() <https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.html#water_benchmark_hub.benchmarks.register>`_
   function right after the class declaration -- the argument is a *key* that is used to load
   the benchmark (resource), which is usually similar (but nicely formatted) to the unique ID of
   the benchmark resource as used in the database.
3. Also, in all cases, the new class must be decoratated with the
   `@meta_data() <https://waterbenchmarkhub.readthedocs.io/en/latest/water_benchmark_hub.html#water_benchmark_hub.meta_data.meta_data>`_
   decorator -- the argument is the unique ID of the benchmark resource as used in the database.
