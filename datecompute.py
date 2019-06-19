#!usr/bin/python3.7
# UTF8
# Date: Mon 27 May 2019 22:30:04 CEST 
# Author: Nicolas Flandrois

import datetime

class DateCount(object):
	"""docstring for DateCount"""
		
	def datenow():
		"""Docstring"""
		ref_a = datetime.date(1970, 1, 1) 
		#Choosen as ref point, as this date is Unix Time = 0
		ref_b = 2062545 #Long Count Base(20): 0.0.0.0.0.12.17.16.7.5 
		#which can be translated into base(20) = CHG75
		#Decimal (base 10) value of maya long count's ref point
		today = datetime.date.today()
		delta = today - ref_a
		#Decimal value of maya long count for today
		dec_lc_today = ref_b + delta.days
		#Then convert this decimal into base(20)
		return dec_lc_today