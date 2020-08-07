# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:27:53 2020

@author: Xp
"""




temp = []
cont = 0
suma = 0
n = int(input("Ingrese la cantidad de temperaturas [1,10]: "))
print("\n")
for i in range(n):
    cont = cont + 1
    num = int(input("Temperatura %d en (C): "%cont))
    temp.append(num)
cGaseoso = 0
cLiquido = 0
cSolido = 0
for num in temp:
        if (num == 100 or num > 100):
            cGaseoso += 1
        elif (num<0 or num == 0):
            cSolido += 1
        elif (num>0 or num < 100):
           cLiquido += 1
suma = suma + num
prom1 = suma*(2) - 10
prom2 = suma*(4.7) - 11.3

print("Cantidad de muestras solidas:  ",cSolido)
print("Cantidad de muestras liquidas: ",cLiquido)
print("Cantidad de muestras gaseosas: ",cGaseoso)
print("Temperatura promedio (C): ",prom1)
print("         Temperatura promedio (F): %.1f"%prom2)