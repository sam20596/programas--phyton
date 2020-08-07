# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:42:08 2020

@author: Xp
"""


x=input("enter a number a cojunt ")
x=int(x)
y=1
acumulador =0
while y <= x:
    print(y, end="")
    acumulador+=y
    y=y+1
print("la suma de los numeros es",acumulador)
p=acumulador/x
print(" el promedio es",p)
