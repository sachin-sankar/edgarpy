# EdgarPython

- Python Library to interact with company filings on SEC's EDGAR portal.
- The main objective of the library is to provide a fast, full typed and tested python API to work with EDGAR portal.
- This library is in early development stages (pre-release)
- The features with the library at this moment is very little. More will be added in the coming versions.
- Once full API support is reached the library will roll into major version releases.

# Installation

Install the library from PyPi using

```shell
pip install edgarpython
```

# Getting Started

To get submissions on EDGAR by Amazon Inc.

```py
from edgar.secapi import getSubmissionsByCik

subs = getSubmissionsByCik("0001018724")
print(subs[0])
```

Every object in the library is a validated and generated using [Pydantic](https://docs.pydantic.dev/latest/)

# Documentation

## `getSubmissionsByCik`

### Params

CIK : `str` - The central index key on the EDGAR portal for a given company.

### Returns

`List[Submission]`

### Raises

`InvalidCik` if the CIK is invalid (404 response)

## `getXlsxUrl`

### Params

CIK : `str` - The central index key on the EDGAR portal for a given company.
accessionNumber : `str` - 18 Digit key for the submission.

### Returns

`str` - URL for the XLSX file if exists for the given accessionNumber

### Raises

`FileNotFoundError` if no XLSX file exists.

## Models

## `Submission`

#### Attributes

- form : `str` - Form name of the submission if available
- accessionNumber : `str` - 18 Digit key for the submission.

# Developing

Contributors are welcome to fork this repo and improve it but please make detailed PRs.
The project is manged using [Poetry](https://python-poetry.org/) and uses [Tox](https://tox.wiki/) and [Pytest](https://docs.pytest.org/en/stable/) for testing.

## Setup

1. Create a virtual environment

```shell
python3 -m venv env
```

2. Activate the `venv`

```shell
source env/bin/activate
```

3. Install required development dependencies

```shell
pip install poetry pytest tox
```

4. Run `poetry install` to complete the setup

## Testing

- Write tests under `/tests` following the convention for the filename as `test_<moduleName>.py`
- For tests inside module test files use `test_<funcName>.py`
- Run the tests using `tox` command.
