# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:54:06 2020

@author: Xp
"""



auxiliar=str()
nombre=str()
vector=[str()for ind0 in range(100)]
print("ingrese el tamaño del vector")
tamanovector=int(input())
for i in range(1,tamanovector+1):
    print("ingrese el nombre del estudiante",i)
    nombre=input()
    vector[i-1]=nombre
    print("el valor en la posicion",i,"es",vector[i-1])
for j in range(1,tamanovector+1):
    for l in range(1,tamanovector):
        if vector[l-1]>vector[l]:
            auxiliar=vector[l-1]
            vector[l-1]=vector[l]
            vector[l]=auxiliar
for k in range(1,tamanovector+1):
    print("el vector ordenado en la posicion",k,"es",vector[k-1])
    
    