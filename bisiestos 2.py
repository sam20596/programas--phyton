# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:14:11 2020

@author: Xp
"""


def isYearLeap(año):
	if año % 4 != 0:
		return False
	elif año % 100 != 0:
		return True
	elif año % 400 != 0:
		return False
	else:
		return True

def daysInMonth(año,mes):
	if año < 1582 or mes < 1 or mes > 12:
		return None
	dia = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = dia[mes - 1]
	if mes == 2 and isYearLeap(año):
		res = 29
	return res

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")