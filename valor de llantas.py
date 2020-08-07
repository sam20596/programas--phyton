# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:07:57 2020

@author: Xp
"""

#uso de condicional simple solo para verdadero 
llantas=input("cantidad de llantas:")
#se pide el valor de llantas a comprar
llantas=int(llantas)
#convertimos el valor a entero 
precio=input("precio unitario:")
#se pide el precio por cada llanta
precio=int(precio)
#convertimos el valor a entero 
if llantas>4:#si la cantida de llantas es mayor a 4
    v=(llantas*precio)-((llantas*precio)/10)
    #se descueta el 10% de valor total
    print ("valor a pagar",v)
    #se imprime el valor 
else:#pero sino no se realizar ningun descuento
    v = llantas*precio
    #formula sin descuento 
    print("valor a pagar",v)
    #se imprime el valor a pagar 


    
    
    






