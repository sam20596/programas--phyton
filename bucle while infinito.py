# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:00:20 2020

@author: Xp
"""


x=input("ingresa numero")
x=int(x)
y=1
acumulador=0
while True:
    print(y)
    acumulador+=y
    y=y+1
    if y>x:
        break
print("la suma es ",acumulador)
p=acumulador/x
print(" el promedio es",p)