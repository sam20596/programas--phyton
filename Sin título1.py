# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:13:37 2020

@author: Xp
"""


x=int(0)
y=int(1)
n=input("ingrese un numero")
print(str(x),""+str(y),end="")
for d in range (2,n):
    v=x+y
    x=y
    y=v
    print(v,end="\t")
    print("") 