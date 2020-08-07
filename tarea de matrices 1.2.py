# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:11:26 2020

@author: Xp
"""


fila = 3
columna = 3
 
matriz =[]
for i in range(fila):
    matriz.append([0]*columna)
print (matriz)
 
##les da valor a la matriz 1a9
contador=1
for i in range(fila):
    for j in range(columna):
        matriz[i][j]=contador
        contador+=1
print(matriz)
 
## ordena la matriz
 
for k in matriz:
    print (k)
 
##Diagonal principal
a=[]
for i in range(fila):
    a.append(matriz[i][i])
print(a)
 
##Diagonal secundaria
a=[]
for i in range(fila):
    a.append(matriz[i][(columna-1)-i])
print(a)