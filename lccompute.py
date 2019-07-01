#!/usr/bin/python3
# UTF8
# Date: Wed 19 Jun 2019 16:00:45 CEST 
# Author: Nicolas Flandrois

from datecompute import Convert
from basecompute import Base

class Longcount(object):
    """We are managing here all Mayan Long Count computations."""
        
    def mayanlc(date):
        """Converting a date argument into a Mayan Long Count's dictionary."""

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

        return mlc

    def mayanlc_display(mlc:dict):
        """Printing a Display of the Mayan Long Count, from dictionary:
        mlc = {"kin":0, "winal":0, "tun":0, "katun":0, "baktun":0, "piktun":0,
               "kalabtun":0, "kinchiltun":0, "alautun":0, "alautun_rest":0}"""
        return f'{mlc["alautun_rest"]}.{mlc["alautun"]}.{mlc["kinchiltun"]}.\
{mlc["kalabtun"]}.{mlc["piktun"]}.{mlc["baktun"]}.{mlc["katun"]}.\
{mlc["tun"]}.{mlc["winal"]}.{mlc["kin"]}'

    def mayanlc_input():
        """The User will be asked for the Mayan LC date in a certain format.
        The Function will output a mcl dictionary"""
        
        mlc = {"kin":0, "winal":0, "tun":0, "katun":0, "baktun":0, "piktun":0,
               "kalabtun":0, "kinchiltun":0, "alautun":0, "alautun_rest":0}

        while True:
            mlcstr = str(input("Please input the Mayan Long Count date.\n\
(Format to Use: 0.0.0.0.0.13.0.6.10.12)\n\n"))

            res = [int(i) for i in mlcstr.replace(".", " ").split()
                   if i.isdigit()]

            try:
                if len(res) == 10:
                    mlc["kin"] = res[9]
                    mlc["winal"] = res[8]
                    mlc["tun"] = res[7]
                    mlc["katun"] = res[6]
                    mlc["baktun"] = res[5]
                    mlc["piktun"] = res[4]
                    mlc["kalabtun"] = res[3]
                    mlc["kinchiltun"] = res[2]
                    mlc["alautun"] = res[1]
                    mlc["alautun_rest"] = res[0]   
                    break

                else:
                    raise

            except:
                print("The value you entered isn't valid.")

        return mlc
