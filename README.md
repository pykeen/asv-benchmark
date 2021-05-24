# Benchmarks for pykeen

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Benchmarks using the [airspeed velocity](https://asv.readthedocs.io/en/stable/index.html) library.

## Installation

```shell
$ pip install -r requirements.txt
```

## Usage

cf. https://asv.readthedocs.io/en/stable/using.html

### Run benchmark

The following command runs the benchmark from the current master branch
of PyKEEN:

```shell
$ asv run
```

The results are stored under `./results`.

### Show results

```shell
$ asv show
```

### Publish results

This creates HTML pages of the report in the `./html` directory.

```shell
$ asv publish
```
