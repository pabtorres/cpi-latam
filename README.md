# cpi-latam
[![PyPI version fury.io](https://badge.fury.io/py/cpilatam.svg)](https://pypi.python.org/pypi/cpilatam/)
[![PyPI download month](https://img.shields.io/pypi/dm/cpilatam.svg)](https://pypi.python.org/pypi/cpilatam/)
[![GitHub license](https://img.shields.io/github/license/stgoa/cpi-latam.svg)](https://github.com/stgoa/cpi-latam/blob/main/LICENSE)
[![Passing](https://github.com/stgoa/cpi-latam/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/stgoa/cpi-latam/actions/workflows/ci.yml)

`cpi-latam` is a Python library designed to simplify the retrieval of Consumer Price Index (CPI) values from the central banks of countries in Latin America

Available countries:
- Perú 🇵🇪
- Colombia 🇨🇴

## Installation
```python
pip install cpilatam
```
## Usage
```python
from cpilatam import DF_CPI

# Retrieve CPI data for Peru
print(DF_CPI["peru"])

# Retrieve CPI data for Colombia
print(DF_CPI["colombia"])
```
## Update CPI Data
Keep your CPI data up-to-date by using the following update function:
```python
from cpilatam import update
update()
```
### Notes:
- Ensure you have an active internet connection for successful data retrieval.
- The library is currently designed to support data from Peru and Colombia only. Future updates may include additional countries.
- For the latest features and improvements, check the GitHub repository.
