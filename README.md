# Currency Converter API

This API provides information for converting values between different currencies. Currently, it supports the following currencies in relation to the Brazilian Real (BRL):

- United States Dollar (USD)
- Euro (EUR)
- Bitcoin (BTC)
- Ethereum (ETH)

## Prerequisites
Before you begin, you will need to have the following tools installed on your machine: Git and Python. Additionally, it is recommended to have an editor for working with the code, such as VSCode.

## Installation

These instructions will allow you to get a copy of the project up and running on your local machine for development purposes.

Install a virtual environment using the terminal:
```bash
pip3 install virtualenv
```

Create a virtualenv:
```bash
python3 -m virtualenv <venv>
```

Activate the virtualenv:

```bash
. venv/bin/activate
```

Open the code editor:
```bash
 code .
```

Install the required packages:
```bash
venv/bin/pip3 install -r requirements.txt
```

Start the server and run project:
```bash
 python3 app.py
```

## Usage

Use the following routes to access the values:
- `/dollar_real/`
- `/euro_real/`
- `/bit_real/`
- `/eth_real/`


## Technologies

The following tools were used in the construction of the project:

- Python - The chosen programming language
- Flask - The web framework used
- AwesomeAPI - The consumed API

## Authors

Alyne Perez - Coding and Documentation - @dev-perez

## Expressions of Gratitude
I appreciate the learning opportunity and the chance to apply what I have been studying.

## License

[MIT](https://choosealicense.com/licenses/mit/)