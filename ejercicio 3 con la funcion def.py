# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:57 2020

@author: Xp
"""


def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("su direccion es:","su sector es:",sector,"la calle es:",calle,)
    print("su casa es la numero:",numcasa,"con codigo postal numero:",codigopostal,)
    print("y esta cerca de :",referencia)
    
    
print("ingrese los datos de direccion que se solicita")
c=input("ingrese la calle de")
s=input("ingrese secto de recidencia")
cod=input("digita tu codigo portal:")
r=input("igresa una referencia")
num=input("ingresa tu numero de casa.")

direccion(c,s,cod,r,num)

    