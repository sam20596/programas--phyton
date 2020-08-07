# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:22:11 2020

@author: Xp
"""


from random import randint
from time import sleep
auxiliar=int()
vector =[int()for ind0 in range(100)]
print("ingrese tamaño del vector")
tamanovector=int(input())
for i in range (1,tamanovector +1):
    vector[i-1]=randint(0,99)
    print("el valor en la posicion",i,"es",vector[i-1])
    sleep(1)
sleep(1)
for j in range(1,tamanovector+1):
    for l in range(1,tamanovector):
        if vector[l+1]>vector[l]:
            auxiliar=vector[l+1]
            vector[l+1]=vector[l]
            vector[l]=auxiliar
for k in range(1,tamanovector+1):
    print("el vector ordenado en la posicion",k,"es",vector[k-1])
    sleep(1)