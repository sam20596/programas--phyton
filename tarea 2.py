# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:38:29 2020

@author: Xp
"""


nombre=input("ingresa tu primer nombre:")
print("hola",nombre)
edad=input("cual es tu edad:")
edad=int(edad)
if edad>=1 and edad<=12:
    print("es niño")
elif edad>=12 and edad <=18:
    print("es adolecente")
elif edad>=18 and edad<=30:
    print("es adulto")
else:
    print("es adulto mayor")
ciudad=input("donde naciste:")
print(ciudad)
print(nombre,edad,ciudad)
