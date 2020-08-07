# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:24:05 2020

@author: Xp
"""
#uso de condicional dobles para verdadero y falso 
h=input("horas trabajadas")
#se pide el ingreso de horas trabajadas 
h=int(h)#convertimos a entero 
t=input("tarifa por hora")
#se pide el ingreso de la tarifa por hora
t=int(t)#convertimos a entero 
d=input("descuento")#se pide el descuento
d=int(d)#converitmos a entero 
if h>40:#si las horas trabajasdas es mayor a 40
    v=((40*4)+((h-40)*6)) - d#se tuiliza la siguiente formula
    print("valor a pagar:",v)# se imprime el valor 
else:# pero si no cumple con la condicion
    v=(h*t)-d#se utiliza la siguiente formula
    print("el valor  a pagar es:",v)# y se imprime el valor 

