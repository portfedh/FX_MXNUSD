# Script to display the MXN:USD exchange rate
# For a given time period in the terminal

# Imports
#########
import os
import requests
import pandas as pd

# Get the API Token
#####################
api_token = os.environ.get("token_banxico")
# api_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Alternative


# Function to download data
###########################
def download_banxico(series, start_date, end_date, token):
    www = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
    url = (www
           + series
           + "/datos/"
           + start_date
           + "/"
           + end_date
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
        # global df
        # Hacemos que la variable global para poder accesarla despues
        
        # Create a dataframe from the data
        df = pd.DataFrame(data)
        # Transform values from strings to floats
        df["dato"] = df["dato"].apply(lambda x: float(x))
        # Transform dates from strings to datetime
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
        # Rename columns
        df.columns = ['Date', 'Exchange Rate']
        return(df)
    # If status fails:
    else:
        # Print the error for user to debug
        print(status)


if __name__ == '__main__':

    # Defining the date Range
    #########################
    print("\nThis script will fetch the official MXN:USD exchange rate for a period: \n")
    start_date = input("Input the start date yyyy-mm-dd: ")
    end_date = input("Input the end date yyyy-mm-dd: ")

    # Determining API series: 'Para solventar Obligaciones'
    #######################################################    
    obligaciones = "SF60653"

    # Execute the function
    ######################
    df = download_banxico(obligaciones,
                          str(start_date),
                          str(end_date),
                          api_token)

    # Display the data in the terminal
    ##################################
    print("\n")
    print(df.to_string(index=False))
    print("\n")
