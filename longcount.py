#!usr/bin/python3.7
# UTF8
# Date: Wed 19 Jun 2019 16:00:45 CEST 
# Author: Nicolas Flandrois

from datecompute import Convert
from basecompute import Base

def mayanlc(date):
	"""Display of the Mayan Long Count"""
	mlc = {"kin":0, "winal":0, "tun":0, "katun":0, "baktun":0, "piktun":0,
		   "kalabtun":0, "kinchiltun":0, "alautun":0, "alautun_rest":0}

	# 20 K'in
	mlc["kin"] = Base.base10toN(Convert.convertor(date), 20)[1]
	kin_rest = Base.base10toN(Convert.convertor(date), 20)[0]

	# 18 Winal
	mlc["winal"] = Base.base10toN(kin_rest, 18)[1]
	winal_rest = Base.base10toN(kin_rest, 18)[0]

	# 20 Tun
	mlc["tun"] = Base.base10toN(winal_rest, 20)[1]
	tun_rest = Base.base10toN(winal_rest, 20)[0]

	# 20 K'atun
	mlc["katun"] = Base.base10toN(tun_rest, 20)[1]
	katun_rest = Base.base10toN(tun_rest, 20)[0]

	# 20 B'ak'tun
	mlc["baktun"] = Base.base10toN(katun_rest, 20)[1]
	baktun_rest = Base.base10toN(katun_rest, 20)[0]

	# 20 Piktun
	mlc["piktun"] = Base.base10toN(baktun_rest, 20)[1]
	piktun_rest = Base.base10toN(baktun_rest, 20)[0]

	# 20 Kalabtun
	mlc["kalabtun"] = Base.base10toN(piktun_rest, 20)[1]
	kalabtun_rest = Base.base10toN(piktun_rest, 20)[0]

	# 20 K'inchiltun
	mlc["kinchiltun"] = Base.base10toN(kalabtun_rest, 20)[1]
	kinchiltun_rest = Base.base10toN(kalabtun_rest, 20)[0]

	# 20 Alautun
	mlc["alautun"] = Base.base10toN(kinchiltun_rest, 20)[1]
	mlc["alautun_rest"] = Base.base10toN(kinchiltun_rest, 20)[0]

	return f'{mlc["alautun_rest"]}.{mlc["alautun"]}.{mlc["kinchiltun"]}.\
{mlc["kalabtun"]}.{mlc["piktun"]}.{mlc["baktun"]}.{mlc["katun"]}.\
{mlc["tun"]}.{mlc["winal"]}.{mlc["kin"]}'

# TEST
print("Mayan Date Now : ")
print(Convert.nowdate())
print(mayanlc(Convert.nowdate()))
print("\nConverting an input date to MLC: (1960-01-02)")
print(mayanlc(Convert.inputdate(1960, 1, 2)))

# ToDo:
# [X] Appending a dictionary to store the Mayan Date
# [ ] Translating the Mayan Date Back into a date
# [ ] Managing the convertions into 2 commands:
#                [ ] Auto Converting Today's date into a Mayan Long Count.
#                       > automayalc() function
#                [ ] Converting a Manually input date into Mayan LC.
#                       > convertmayalc() function
#                [ ] Translating a Manually input Mayan LC into a data.
#                       > translatemayalc() function