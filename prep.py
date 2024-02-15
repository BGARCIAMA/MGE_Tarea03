# prep.py
'''Este script prepara los datos para incorporarlos al modelo
    Las funciones dentro de este script son:
    - descargar_datos
    - impute_continuous_missing_data
    - preprocesar_datos
'''
#Importa las librerias
import pandas as pd
from src import script

#Descarga los datos
data_total = script.descargar_datos("data/raw/train.csv","data/raw/test.csv" )

#Preprocesa los datos
script.impute_continuous_missing_data(passed_col)
data_final = script.preprocesar_datos(data_total)

#Guarda los datos
pd.DataFrame(data_total).to_csv("data/prep/data_total.csv", index=False)
pd.DataFrame(data_final).to_csv("data/prep/data_final.csv", index=False)
