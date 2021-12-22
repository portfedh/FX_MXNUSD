# Importing Modules
######################
# Sacar las enviroment variables (token de Banxico)
import os
# Enviar HTTP requests usando python
import requests
# Transformar los datos en un DataFrame
import pandas as pd

# Fechas para el calculo
########################
print("\n Busqueda de FX para Solventar Obligaciones: \n")

# Fecha Inicial
fecha_inicial = input("Fecha Inicial de Busqueda yyyy-mm-dd: ")

# Fecha Final
fecha_final = input("Fecha Final de Busqueda yyyy-mm-dd: ")

# Conexion a Banxico
####################

# Token de Consulta Banxico
token = os.environ.get("token_banxico")

# Clave de Descarga Banxico
obligaciones = "SF60653"  # FX Para Solventar Obligaciones

# Descargando datos de Banxico
##############################


# Funcion de Descarga
def descarga_bmx_serie(serie, fechainicio, fechafin, token):
    # Al site de banxico se le pegan los datos de consulta
    url = ("https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
           + serie+"/datos/"+fechainicio+"/"+fechafin)

    # Se le tienen que pasar Headers
    # Se pasa el token de banxico en un diccionario.
    # Se pasa como un Request con metodo Get
    # Se le solicita el codigo de respuesta al servidor.
    headers = {"Bmx-Token": token}
    response = requests.get(url, headers=headers)
    status = response.status_code

    # Si el estatus esta Ok armar el dataframe
    # Si el estatus esta mal imprimir el Error en la consulta.
    if status == 200:
        # Si el codigo es correcto pasa la respuesta a formato Json
        raw_data = response.json()

        # Pasamos las llaves en el Json para crear la serie de datos.
        data = raw_data["bmx"]["series"][0]["datos"]

        # Creamos con la serie un dataframe
        # Volvemos los datos floats en vez de strings
        # Volvemos las fechas a formato fecha
        # Volvemos la fecha la columna indice (Deshabilidado)
        # Regresa el Dataframe
        # Cambia el nombre de la columna "dato"  por tipo de cambio
        global df
        df = pd.DataFrame(data)
        df["dato"] = df["dato"].apply(lambda x: float(x))
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
        # df.set_index("fecha", inplace = True)
        df.columns = ['Fecha', 'Tipo de Cambio']
        return(df)
    else:
        print(status)


# Ejecutando la Solicitud de Descarga
#####################################
dolares_bmx = (descarga_bmx_serie(obligaciones,
               str(fecha_inicial), str(fecha_final), token))


# Mostramos la informacion sin el indice
########################################
print("\n")
print(df.to_string(index=False))
print("\n")
