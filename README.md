# DFGraph
[![pip](https://img.shields.io/pypi/v/dfgraph.svg?maxAge=3600)](https://pypi.org/project/dfgraph/)
[![DOI](https://zenodo.org/badge/360189302.svg)](https://zenodo.org/badge/latestdoi/360189302)
![workflow](https://github.com/willi-z/dfgraph/actions/workflows/ci.yml/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/willi-z/dfgraph/branch/master/graph/badge.svg?token=JVKPGLBT3J)](https://codecov.io/gh/willi-z/dfgraph)

The `directed and flexible graph` is part of [DigiFors](https://digifors.de/) effort
to contribute to the analysing and detection of content and context dependent information.
'DFGraph' is a simple, but powerful graph based database library based on the `sqlalchemy` library.
Its main purpose is to store data from large datasets and allows manipulate, connect and detect content.
This allows for more flexible conversion and detection processes.  

## Installation

`pip install dfgraph`

## Usage

See the `examples/` files for some simple use-cases and implementations.

## Testing
till `pip 21.3`:
```
pip install --use-feature=in-tree-build -e .
```
`pip 21.3+`:
```
pip install -e .
```

```
coverage run --source=src -m pytest && coverage report -m
```

## Usage

`dfgraph` comes with two main classes: `Node` and `Relationship`.
It was designed to represent Data from Databases 

## Capabilities

Legend:

| Symbol | Meaning                              |
| ------ | ------------------------------------ |
| ✅     | finished                             |
| 🔜     | working on implementation            |
| 🟦     | planned                              |


| Capability                           | Status |
| ------------------------------------ | ------ |
| Nodes and Relations                  | ✅     |
| Graph                                | ✅     |
| Database Storage and Loading         | ✅     |
| Asynchronous Database Interaction    | 🔜     |
| Visualisation                        | 🔜     |
| Support for Context Detection        | 🔜     |
| Highperformance Queries              | 🟦    |

## Citing this Module

If you use DFGraph for research and would like to cite the module and source, 
you can visit dfgraph Zenodo and generate the correct citation. 
For example, the BibTex citation is:
```
@software{willi_zschiebsch_2021_4748703,
  author       = {Willi Zschiebsch},
  title        = {willi-z/dfgraph: 0.1.3},
  month        = may,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.1.3},
  doi          = {10.5281/zenodo.4748703},
  url          = {https://doi.org/10.5281/zenodo.4748703}
}
```
Please visit the [link](https://zenodo.org/badge/latestdoi/360189302) above for the most recent citation as the citation here may not be current.
