# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:21:52 2020

@author: Xp
"""


matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range (0,5):
    for j in range(0,6):
        print("ingrese el valor para la posicions",i,j)
        matrix[i][j]=int(input())
print(matrix)