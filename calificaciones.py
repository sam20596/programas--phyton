# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:59:14 2020

@author: Xp
"""

#uso de condicional multiple 
a=input("ingrese su primera calificacion: ")
#pide el ingreso de la primera calificacion
a=int(a)#convierte en entero 
b=input("ingrese su segunda calificacion: ")
#pide el ingreso de la segunda calificacion
b=int(b)#convierte en entero
c=input("ingrese su tercera calificacion: ")
#pide el ingreso de la segunda calificacion 
c=int(c)#convierte en entero 
if a>b and c>b:#condicion cuando a y c sena mayores
    d=a+c#formula a trabajar
    print("su calificacion total es: " , d)
    #imprime el valor 
elif a>c and b>c:#condicion en la que a y b sean mayores
    
    d=a+b#formula a trabajar
    print("su calificacion total es: "  ,d)
     #imprime valor 
else:#caso contrario 
    d=b+c#formula a trabajar para falso en condicion 
    print("su calificacion total es: "  ,d)
    #imprime valor 
