# USD/Mexican Peso Official Exchange rate

## What it does

A simple script used to determine the USD:MXN official exchange rate between two periods:

- The user will input an initial and final date.

- The script connects to the Bank of Mexico (Banxico) API. 

- It requests the FX daily rate for the period.

- It then outputs the FX rates in the terminal window.

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

The script may be useful for accountants,  administrative/financial professionals or anyone interested in using official FX rates.

The Bank of Mexico issues 3 types of USD:MXN exchange rates:

- FIX
- DOF
- Obligaciones

FIX: is calculated by taking the average price of all trades up to 12pm. It is used mainly for transactions that an official rate closer to the spot rate.

DOF: (Diario Oficial de la Federacion). The Fix rate is published the next day in the DOF, which is where the Mexican Government makes official publications. Some institutions use DOF rate because its rate can be known beforehand from the FIX rate and can give enough time to prepare for a transaction.

Obligaciones: This rate is the FIX rate from two day prior. It also sets an official FX rate for weekends, hollidays or any non tradable days, where FIX or DOF may not be available. It is the rate used for tax purposes and in dealings with any government institutions in Mexico.

The script is set by default to get the "Obligaciones" FX rate.

If you want to use FIX instead, substitute the following code:

```python
# Before
obligaciones = "SF60653" 

# After
obligaciones = "SF43718" 
```

If you want to use DOF, you will have to modify the code to get the FIX rate from the previous day.

## Contributing

Any help making the scripto into an executable file for windows and mac would be very helpful. 

This would allow non-programmers to use it. 
