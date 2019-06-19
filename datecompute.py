#!usr/bin/python3.7
# UTF8
# Date: Mon 27 May 2019 22:30:04 CEST 
# Author: Nicolas Flandrois

import datetime

class Convert(object):
	"""Convert will regroup functions managing dates."""
	
	def nowdate():
		"""Date now"""
		return datetime.date.today()

	def inputdate(year, month, day):
		"""Formating the date into a computable format."""
		return datetime.date(year, month, day)

	def convertor(datedata):
		"""Issuing the date now as a decimal integer ready to be converted 
		into Mayan count bases (Base-20 and Base-18)"""
		ref_a = datetime.date(1970, 1, 1) 
			# Choosen as ref point, as this date is Unix Time = 0
		ref_b = 1856305 #Long Count Base(20): 0.0.0.0.0.12.17.16.7.5 
			# which can be translated into base(20) = CHG75
			# Decimal (base 10) value of maya long count's ref point
		delta = datedata - ref_a
			# Decimal value of maya long count for today
			# Then convert this decimal into base(20)
		return ref_b + delta.days

# Test
# print("Computing Today's date Automaticaly")
# print("Auto Dating Now: ", Convert.nowdate())
# print("Converting the date: ", Convert.convertor(Convert.nowdate()))
# print("Computing an Input Date")
# print("Formating the date : ", Convert.inputdate(1970, 7, 2))
# print("Converting the date : ", Convert.convertor(
# 	  Convert.inputdate(1970, 7, 2)))