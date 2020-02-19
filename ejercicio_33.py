# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:37:57 2020

@author: Felipe Robles
"""

#Ejercicio

#Realize un query sobre los datos que desea analizar con 
#datos de precios de varios años

#Revise la distribución de sus datos con la función describe().

#Calcule la correlación por pares entre sus variables 
#usando la función corr () .


import numpy as np
import pandas as pd

import sqlite3
from IPython.display import display, HTML

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("guia_fasecolda.sqlite")

#ESCRIBE LA CONSULTA DE LO QUE DESEAS ANALIZAR
#df = pd.read_sql_query('SELECT Marca,Referencia1,Cilindraje,Peso,"2015","2016","2017" FROM carros where Cilindraje<1500 AND Cilindraje>1200 AND "2015">0;', con)
df = pd.read_sql_query('SELECT Marca,Referencia1,Cilindraje,Peso,"2015","2016","2017" FROM carros', con)


print("Total de memoria ram requerida ",df.memory_usage().sum())
print(df)
#estadistica descriptiva
display(HTML(df.describe().to_html()))
#correlación entre las columnas
display(HTML(df.corr().to_html()))

con.close()