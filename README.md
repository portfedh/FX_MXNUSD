# USD/Mexican Peso Official Exchange rate

## What it does

A simple script used to determine the USD:MXN official exchange rate between two periods:

- The user will input an initial and final date.

- The script will connect to the Bank of Mexico's (Banxico) API.

- It will request the exchange rate for the selected dates.

- It will then display the exchange rates in the terminal window.

### How to Install

To use this script, you must have previously installed:

- Python 3
- Pandas
- Requests

You will also need a (free) API token from Banxico, which can be obtained here:
[API Banxico Spanish](https://www.banxico.org.mx/SieAPIRest/service/v1/)
[API Banxico English](https://www.banxico.org.mx/SieAPIRest/service/v1/?locale=en)

Once you have the API token substitute it in the Token variable:

```python
# Before
token = os.environ.get("token_banxico")

# After
token = "<paste_your_token_here>"
```

You can then run the python script from your terminal.

If you upload the script to any public repository, It is recommend saving the token as an environment variable for security reasons.

If you use this information frequently you can add an alias in your bash.rc, .zshrc or wherever you store aliases in your operating system to call the script in a simpler way.

## How to Use

Simply execute the script from your terminal:

```bash
# Spanish
python3 fx_get_terminal.py

# English
python3 fx_get_terminal_en.py
```

When run, the script will ask for a start and end date

The script will then retrieve the daily fx values for the time period.

Output will display the FX rates for the period.

<img src="https://bite-size.mx/fx_terminal.gif" alt="<fx_terminal" width="600" height="392">

## Use cases

The script may be useful for accountants, administrative, financial professionals or anyone interested in using official FX rates that are valid for tax purposes.

The Bank of Mexico issues 3 types of USD:MXN exchange rates:

- FIX
- DOF
- Obligaciones

FIX: is calculated by taking the average price of all trades up to 12pm. It is used mainly for transactions that an official rate closer to the spot rate.

DOF: (Diario Oficial de la Federacion). The Fix rate is published the next day in the DOF, which is where the Mexican Government makes official publications. Some institutions use DOF rate because its rate can be known beforehand from the FIX rate and can give enough time to prepare for a transaction.

Obligaciones: This rate is the FIX rate from two day prior. It also sets an official FX rate for weekends, holidays or any non tradable days, where FIX or DOF may not be available. It is the rate used for tax purposes and in dealings with any government institutions in Mexico.

You can find a more in depth explanation of the difference in FX rates here:
[Understanding the MXN:USD exchange rate](https://pablocruz.io/how-to-get-the-official-usd-mxn-exchange-rate-from-banxico/)

The script is set by default to get the "Obligaciones" FX rate.

If you want to use FIX instead, substitute the following code:

```python
# Before (Obligaciones)
obligaciones = "SF60653" 

# After (FIX)
obligaciones = "SF43718" 
```

If you want to use DOF, you will have to modify the code to get the FIX rate from the previous day.

## Contributing

Any help making the scrip to into an executable file for windows and mac would be very helpful.

This would allow non-programmers to use it.
