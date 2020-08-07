# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:56:01 2020

@author: Xp
"""


nombre=input("Ingresa tu nombre:")
apellido=input("Ingresa tu apellido:")
localidad=input("Ingresa tu localidad:")
edad=input("Ingresa tu edad:")
edad=int(edad)
if edad>=1 and edad<=12:
    print("es niño")
elif edad>=12 and edad <=18:
    print("es adolecente")
elif edad>=18 and edad<=30:
    print("es adulto")
else:
    print("es adulto mayor")
space=" "
print("YO SOY " , space , nombre , space , apellido , space , "VIVO EN" , space , localidad , space , "Y TENGO", space , edad , space , "AÑOS" )
