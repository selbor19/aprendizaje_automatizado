# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:37:57 2020

@author: Felipe Robles
"""

import numpy as np
 

#sumarlos
#concatenar los dos arreglos
#encontrar la sumatoria de los valores
#encontrar la media de los valores
#imprimir los numeros mayores que 5
#determinar las posiciones de los numeros que son iguales en los arreglos

#CREAR DOS VECTORES DE DIEZ NUMEROS ALEATORIOS ENTEROS
ArrayA = np.random.randint(low=1,high=10,size=10)
print(ArrayA)
ArrayB = np.random.randint(low=1,high=10,size=10)
print(ArrayB)
print (type(ArrayA))
print (type(ArrayB))

#SUMARLOS

np_sum = ArrayA + ArrayB
print("Suma de vectores =  ", np_sum)

#CONCATENAR LOS DOS ARREGLOS
np_conca = np.concatenate((ArrayA,ArrayB), axis=0)
print ("vectores concatenados = ",np_conca)
 
#ENCONTRAR LA MEDIA DE LOS VALORES
np_medianA = np.median(ArrayA)
np_medianB = np.median(ArrayB)
print ("La media del arreglo A es = ",np_medianA)
print ("La media del arreglo B es = ",np_medianB)

#IMPRIMIR LOS NUMERO > 5

np_where_A = np.where(ArrayA > 5)
np_where_B = np.where(ArrayB > 5)
print(np_where_A)
print(np_where_B)

# DETERMINAR LAS POSICIONES DE LOS NUMEROS QUE SON IGUALES EN LOS ARREGLOS







