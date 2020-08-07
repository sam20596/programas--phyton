# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:54:17 2020

@author: Xp
"""


import numpy as np
a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("\n"*2)
c=np.ones((4,4))
print(c)
print("\n"*2)
d=np.ones((4,2))
print(d)
print("\n"*2)
print(c.dot(d))
print("\n"*2)
print(np.dot(c,d))
