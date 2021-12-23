# Programa para mostrar el tipo de cambio MXN:USD
# Para un periodo de fechas.

# Imports del Programa
######################
import os
import requests
import pandas as pd

# Fechas para el calculo
########################
print("\n Busqueda de FX para Solventar Obligaciones: \n")
fecha_inicial = input("Fecha Inicial de Busqueda yyyy-mm-dd: ")
fecha_final = input("Fecha Final de Busqueda yyyy-mm-dd: ")

# Conexion a Banxico
####################
token = os.environ.get("token_banxico")
# Token de Consulta Banxico
obligaciones = "SF60653"  # FX Para Solventar Obligaciones
# Clave de Descarga Banxico

# Descargando datos de Banxico
##############################


# Funcion de Descarga de datos de Banxico
def descarga_bmx_serie(serie, fechainicio, fechafin, token):
    # Al site de banxico se le pegan los datos de consulta
    url = ("https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
           + serie
           + "/datos/"
           + fechainicio
           + "/"
           + fechafin
           )
    # Se le tienen que pasar Headers
    headers = {"Bmx-Token": token}
    # Se pasa como un request con metodo get
    response = requests.get(url, headers=headers)
    # Se le solicita el codigo de respuesta al servidor.
    status = response.status_code
    if status == 200:
    # Si el estatus esta Ok crear el dataframe
        raw_data = response.json()
        # Se guarda la respuesta como una variable.
        data = raw_data["bmx"]["series"][0]["datos"]
        # Se filtra el json
        # Se accesa el diccionario con los datos
        global df
        df = pd.DataFrame(data)
        # Creamos un dataframe con la infrmacion
        df["dato"] = df["dato"].apply(lambda x: float(x))
        # Volvemos los datos floats en vez de strings
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
        # Volvemos las fechas a formato fecha
        df.columns = ['Fecha', 'Tipo de Cambio']
        # Cambia el nombre de la columna "dato"  por tipo de cambio
        return(df)
    else:
    # Si el estatus esta mal imprimir el prror en la terminal
        print(status)


# Ejecutando la Solicitud de Descarga
#####################################
dolares_bmx = descarga_bmx_serie(obligaciones,
                                 str(fecha_inicial),
                                 str(fecha_final),
                                 token)


# Mostramos la informacion sin el indice
########################################
print("\n")
print(df.to_string(index=False))
print("\n")
