# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:19:58 2020

@author: Xp
"""


#crear un scrip donde nos permita ingresar el valor de filas y columna
#de una mattriz e imprimir las diagonales 
from random import randint

n=print("ingese el numero de filas")
n=int(input())

m=print("ingrese el numero de columnas ")
m=int(input())
import numpy as np
matriz=np.random.random((n,m))

contador=0
for i in range(n):
    for j in range(m):
        matriz[i][j]=randint(0, 99)
        contador+=1
print(matriz)
 #DIAGONAL PRINCIPAL
a=[]

for i in range(n):
    a.append(matriz[i][i])
print("la diagonal principal es",a)
 
#DIAGONAL SECUNDARIA
a=[]
for i in range(n):
    a.append(matriz[i][(m-1)-i])
print("la diagonal secundaria es",a)