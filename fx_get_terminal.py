# Programa para mostrar el tipo de cambio MXN:USD
# Para un periodo de fechas.

# Imports
#########
import os
import requests
import pandas as pd

# Get the API Token
####################
api_token = os.environ.get("token_banxico")
# api_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Alternativa


# Funcion de descarga de datos
##############################
def descarga_banxico(serie, fechainicio, fechafin, token):
    www = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
    url = (www
           + serie
           + "/datos/"
           + fechainicio
           + "/"
           + fechafin
           )
    # Se crea un diccionarion con el token del API
    headers = {"Bmx-Token": token}
    # Hacer un GET request a la pagina del API
    response = requests.get(url, headers=headers)
    # Revisar el codigo de respuesta
    status = response.status_code
    # Si el estatus esta OK:
    if status == 200:
        # Crear un objeto json
        raw_data = response.json()
        # Accesar los datos dentro del objeto json
        data = raw_data["bmx"]["series"][0]["datos"]
        # Creamos un dataframe con los datos
        df = pd.DataFrame(data)
        # Transformamos los datos de strings a floats
        df["dato"] = df["dato"].apply(lambda x: float(x))
        # Transformamos las fechas de strings a datetime
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
        # Renombramos las columnas
        df.columns = ['Fecha', 'Tipo de Cambio']
        return(df)
    # Si el estatus tiene error:
    else:
        # Imprimir el error
        print(status)


if __name__ == '__main__':

    # Fechas para el calculo
    ########################
    print("\nBusqueda de FX para Solventar Obligaciones: \n")
    fecha_inicial = input("Fecha Inicial de Busqueda yyyy-mm-dd: ")
    fecha_final = input("Fecha Final de Busqueda yyyy-mm-dd: ")

    # Determinando la serie: 'Para solventar Obligaciones'
    ######################################################
    obligaciones = "SF60653"

    # Ejecutando the function
    #########################
    df = descarga_banxico(obligaciones,
                          str(fecha_inicial),
                          str(fecha_final),
                          api_token)

    # Mostrar los datos en la terminal
    ##################################
    print("\n")
    print(df.to_string(index=False))
    print("\n")
