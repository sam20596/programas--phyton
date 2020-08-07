# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:32:31 2020

@author: Xp
"""


hostnames=["R1","R2","R3","S1","S2","S3"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[ 0])
print(hostnames[ 1])
print(hostnames[ 2])
print(hostnames[ 3])
print(hostnames[ 4])
print(hostnames[ 5])
hostnames[ 0]="RTR"
del hostnames [ 5]