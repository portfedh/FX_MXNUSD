# Script to display the MXN:USD exchange rate
# For a given time period in the terminal
# Author: Pablo Cruz Lemini

import os
import requests
import pandas as pd

class GetFxTerminal():
    api_token = os.environ.get("token_banxico")
    obligaciones = "SF60653"
    fix = "SF63528"
    www = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/"

    def __init__(self):
        pass

    def get_dates(self):
        print("\nThis script will fetch the official MXN:USD exchange rate for a period: \n")
        self.fecha_inicial = str(input("Input the start date yyyy-mm-dd: "))
        self.fecha_final = str(input("Input the end date yyyy-mm-dd: "))

    def get_data(self, serie, fechainicio, fechafin, token):
        url = (GetFxTerminal.www
            + serie
            + "/datos/"
            + fechainicio
            + "/"
            + fechafin
            )
        # Create a dictionary with the API Token
        headers = {"Bmx-Token": token}
        # Create a GET request to the API
        response = requests.get(url, headers=headers)
        # Check the status code
        status = response.status_code
        # If status code is Ok:
        if status == 200:
            # Return json object
            raw_data = response.json()
            # Access the data inside the object
            data = raw_data["bmx"]["series"][0]["datos"]
            # Create a dataframe from the data
            self.df = pd.DataFrame(data)
            # Transform values from strings to floats
            self.df["dato"] = self.df["dato"].apply(lambda x: float(x))
            # Transform dates from strings to datetime
            self.df["fecha"] = pd.to_datetime(self.df["fecha"], format="%d/%m/%Y")
            # Rename columns
            self.df.columns = ['Date', 'Exchange Rate']
            return self.df
        # If status fails:
        else:
            # Print the error for user to debug
            print(status)

    def print_output(self):
        print("\n")
        print(self.df.to_string(index=False))
        print("\n")


if __name__ == '__main__':
    oGetFx = GetFxTerminal()
    oGetFx.get_dates()
    oGetFx.get_data(
        GetFxTerminal.obligaciones,
        oGetFx.fecha_inicial,
        oGetFx.fecha_final,
        GetFxTerminal.api_token
        )
    oGetFx.print_output()
