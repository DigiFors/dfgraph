# DFGraph
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
