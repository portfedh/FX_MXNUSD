# USD/Mexican Peso Official Exchange rate

## What it does

A simple script used to determine the USD:MXN official exchange rate between two periods.

The user will input an initial and final date.

The program connects through an API to the Bank of Mexico (Banxico) and retreives the FX daily rate for the period.

The script will then output the FX rates in the terminal window.

### How to Install

To use this script, you must have previously installed:

- Python 3
- Pandas
- Requests

You will also need a (free) API token from Banxico, which can be obtained here:
[API Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/)

Once you have the API token subsitute it in the Token variable:

```python
# Before
token = os.environ.get("token_banxico")

# After
token = "<paste_token_here>"
```

You can then run the python script from your terminal.

If you use this information frequently, I recommend adding an alias to the script path to make it simpler to call the script.

## How to Use

When run, the script will ask for a start and end date

The script will then retrieve the daily fx values for the time period.

Output will display the FX rates for the period.

<img src="https://bite-size.mx/fx_terminal.gif" alt="<fx_terminal" width="600" height="392">

## Use cases

The script is useful for accountants or administrative/financial professionals.

The Bank of Mexico issues 3 types of USD:MXN exchange rates:

- FIX
- DOF
- Obligaciones

FIX: is calculated by taking the average level of all trades up to 12pm. It is used mainly for transactions that want to use an official rate which is closer to the spot rate of when a transaction is made.

DOF: (Diario Oficial de la Federacion). The Fix rate is published the next day in the DOF, which is where the Mexican government makes official publications. Some institutions use DOF rate because its rate can be known beforehand from the FIX rate and can give insitutions enough time to prepare for a transaction.

Obligaciones: This rate is the FIX rate from two previous days. It also sets an official FX rate for weekends, hollidays or any non tradable days, where FIX or DOF may not be available. It is the rate used for tax purposes and in dealings with any government institutions.

The script is set by default to get the "Obligaciones" FX rate.

If you want to use FIX, substitute the following.

```python
# Before
obligaciones = "SF60653" 

# After
obligaciones = "SF43718" 
```

If you want to use DOF, you will have to modify the code to get the FIX rate from the previous day.

## Contributing

If you can help making this a simple executable file for windows and mac, so non-programmers can use it, it would be much appreciated.
