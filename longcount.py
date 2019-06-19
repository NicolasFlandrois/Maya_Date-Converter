#!usr/bin/python3.7
# UTF8
# Date: Wed 19 Jun 2019 16:00:45 CEST 
# Author: Nicolas Flandrois

from datecompute import Convert
from basecompute import Base

# 20 K'in
kin = Base.base10toN(Convert.convertor(Convert.nowdate()), 20)[1]
kin_rest = Base.base10toN(Convert.convertor(Convert.nowdate()), 20)[0]
# print(kin)

# 18 Winal
winal = Base.base10toN(kin_rest, 18)[1]
winal_rest = Base.base10toN(kin_rest, 18)[0]
# print(winal)

# 20 Tun
tun = Base.base10toN(winal_rest, 20)[1]
tun_rest = Base.base10toN(winal_rest, 20)[0]
# print(tun)

# 20 K'atun
katun = Base.base10toN(tun_rest, 20)[1]
katun_rest = Base.base10toN(tun_rest, 20)[0]
# print(katun)

# 20 B'ak'tun
baktun = Base.base10toN(katun_rest, 20)[1]
baktun_rest = Base.base10toN(katun_rest, 20)[0]
# print(baktun)

# 20 Piktun
piktun = Base.base10toN(baktun_rest, 20)[1]
piktun_rest = Base.base10toN(baktun_rest, 20)[0]
# print(piktun)

# 20 Kalabtun
kalabtun = Base.base10toN(piktun_rest, 20)[1]
kalabtun_rest = Base.base10toN(piktun_rest, 20)[0]
# print(kalabtun)

# 20 K'inchiltun
kinchiltun = Base.base10toN(kalabtun_rest, 20)[1]
kinchiltun_rest = Base.base10toN(kalabtun_rest, 20)[0]
# print(kinchiltun)

print(f'{kinchiltun}.{kalabtun}.{piktun}.{baktun}.{katun}.{tun}.{winal}.\
{kin}')

# ToDo:
# [ ] Appending a dictionary to store the Mayan Date
# [ ] Translating the Mayan Date Back into a date
# [ ] Managing the convertions into 2 commands:
#                [ ] Auto Converting Today's date into a Mayan Long Count.
#                [ ] Converting a Manually input date into Mayan LC.
#                [ ] Translating a Manually input Mayan LC into a data.