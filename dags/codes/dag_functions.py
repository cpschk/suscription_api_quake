#Importacion de librerias
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
# from pandas.io import sql
# import numpy as np
import requests
from pandas.io.json import json_normalize
from datetime import datetime, timedelta

class QuakeFunctions:
    # def __init__(self):
    #     pass

    def last24hrs():
        """
            Obtener los datos desde el presente a un año atras.
        """
        endtime = datetime.now()  # .strftime("%Y-%m-%d")
        startime = endtime - timedelta(days=1)

        endtime = endtime.strftime("%Y-%m-%d")
        starttime = startime.strftime("%Y-%m-%d")
        print(starttime, endtime)
        return starttime, endtime

    def extract_eartquake(starttime=None, endtime=None):
        #importar los datos desde una api
        url=f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={starttime}&endtime={endtime}&minmagnitude=5"
        respuesta = requests.get(url)
        contenido = respuesta.json()

        # Con pd.json_normalize transformamos el json en un pandas dataframe
        temblores = pd.json_normalize(contenido['features'])

        # quita la palabra "properties." de las nombres de las columnas
        temblores.columns=temblores.columns.str.replace('properties.','', regex=True)
        return temblores

    # def extract_eartquake(starttime=None, endtime=None):
    #     url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={starttime}&endtime={endtime}&minmagnitude=5"

    #     response = requests.get(url)
    #     contenido = response.json()
    #     if response.status_code == 200:
    #         Quake = pd.json_normalize(contenido['features'])
    #         Quake.columns=Quake.columns.str.replace('properties.','', regex=True)
    #         return Quake
    #     else:
    #         return None