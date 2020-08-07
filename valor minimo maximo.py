# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:44:42 2020

@author: Xp
"""


import numpy as np
matrix=np.array([(3,2,1,0),(6,5,4,3)])

print("\n"*2)
print(matrix.min())#valor minimode la matriz
print(matrix.max())#valor maximo de la matriz
print(matrix.sum())#la suma de la matriz 
print(matrix.std())#desviacion estandar de toda la matriz
print(np.sqrt(matrix))#raiz de cada uno de los elementos de la matriz
print(np.std(matrix))#deviacion estandar de cada uno de los elementos de la matriz 