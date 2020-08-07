# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:24:53 2020

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

def daysInMonth(año, mes):
	if año < 1582 or mes < 1 or mes > 12:
		return None
	dia = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = dia[mes - 1]
	if mes == 2 and isYearLeap(año):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2000, 12, 31))