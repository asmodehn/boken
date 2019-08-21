# boken

[![Build Status](https://travis-ci.org/asmodehn/boken.svg?branch=master)](https://travis-ci.org/asmodehn/boken)
[![Updates](https://pyup.io/repos/github/asmodehn/boken/shield.svg)](https://pyup.io/repos/github/asmodehn/boken/)
[![Python 3](https://pyup.io/repos/github/asmodehn/boken/python-3-shield.svg)](https://pyup.io/repos/github/asmodehn/boken/)

Bot for Kraken

## User

### Quickstart
Run a simple simulated strategy locally, but using real data from the exchange, do:
```bash
TODO
```

### Jupyter notebooks
To use this library via a jupyter notebook to quickly get a nice visual feedback, do:
```bash
TODO
```

### Setup
To setup your keys to access your account, do:
```bash
TODO
```
Note : on first start, the ledger for the bot trade is created as a sqlite database.
There is one database per strategy, and it holds all of the state the bot could have and needs to persist between run.
To work interactively with the sqlite DB, do:
```bash
TODO
```

### Run CLI Examples
To run a few commands manually for kraken, do:
```bash
TODO
```
Note the trades made like this will be affected to a specific ledger named "cli"

### Run Strategy
To run a simple strategy, for real, on kraken, do:
```bash
TODO
```

## Developer

### Git
We follow gitflow branching strategy.
Any question/concern, do not hesitate to post an Issue.
Any proposal for improvement, do not hesitate to post a Pull Request.
We will try to prioritize addressing issues and merging PR via milestones.

Disclaimer : We are currently setting up the basis of the code, so this can be messy at the moment...

### Pipenv
We will use the tools that makes it convenient to code interactively in python.
Toolchain:
- pipenv
- pytest
- vcrpy
- mypy
- black
- jupyter
- sphynx

Feel free to propose your favorite tool and argument why it would help to bring in a better interactivity when working with an autonomous software.

### Tests
To run the tests, using prerecorded server response, do:
```bash
pytest
```
This includes typing and doctests.

### Record
To get meaningful server data to test again later, we use vcrpy.
to run the tests and record, do:
```bash
pytest --record-mode=all
```
