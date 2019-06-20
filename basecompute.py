#!usr/bin/python3.7
# UTF8
# Date: Wed 19 Jun 2019 15:28:22 CEST
# Author: Nicolas Flandrois

class Base(object):
    """Base class group functions to compute a number from base 10
    to n-base. As needed for a Mayan Long Count, the output will still be
    displayed using arabic numbers 0-9 (No Letters as number here)."""
        
    def base10toN(n_input, n_base):
        """This function will compute from Base-10 to Base-N"""
        a = n_input//n_base
        b = n_input%n_base
        return a, b 
        # Returns a Tuple (a, b) ('a' (Tiple[0]) will be compute for the next
        # digit, 'b' (Tiple[1]) is the reminder)

    def mlctobase10(mlc:dict):
        """This functions to compute a MayanLC dictionary, to a MayanLC 
        Decimal Integer.

        mlc = {"kin":0, "winal":0, "tun":0, "katun":0, "baktun":0, "piktun":0,
               "kalabtun":0, "kinchiltun":0, "alautun":0, "alautun_rest":0}

        Using the following computation.
        9.12.2.0.16 (Long Count)
          9   × 144000    = 1296000
          12  × 7200  = 86400
          2   × 360   = 720
          0   × 20    = 0
          16  × 1 = 16
          Total (sum) days  = 1383136"""

        kin = mlc["kin"]*1
        winal = mlc["winal"]*20
        tun = mlc["tun"]*360
        katun = mlc["katun"]*7200
        baktun = mlc["baktun"]*144000
        piktun = mlc["piktun"]*2880000
        kalabtun = mlc["kalabtun"]*57600000
        kinchiltun = mlc["kinchiltun"]*1152000000
        alautun = mlc["alautun"]*23040000000
        alautun_rest = mlc["alautun_rest"]*460800000000

        return kin + winal + tun + katun + baktun + piktun + kalabtun +\
               kinchiltun + alautun + alautun_rest


#TEST
# print("base10toN")
# print("Base 20: ", Base.base10toN(50, 20))
# print("Base 18: ", Base.base10toN(50, 18))
# print("baseNto10")
# print("Base 20: ", Base.baseNto10(60, 20))
# print("Base 18: ", Base.baseNto10(40, 18))

# mlc = {"kin":12, "winal":10, "tun":6, "katun":0, "baktun":13, "piktun":0,
#            "kalabtun":0, "kinchiltun":0, "alautun":0, "alautun_rest":0}

# kin = mlc["kin"]
# winal = mlc["winal"]
# tun = mlc["tun"]
# katun = mlc["katun"]
# baktun = mlc["baktun"]
# piktun = mlc["piktun"]
# kalabtun = mlc["kalabtun"]
# kinchiltun = mlc["kinchiltun"]
# alautun = mlc["alautun"]
# alautun_rest = mlc["alautun_rest"]

# print(f"Mayan LC {alautun_rest}.{alautun}.{kinchiltun}.{kalabtun}.{piktun}.\
# {baktun}.{katun}.{tun}.{winal}.{kin}\n\
# Decimal Value is : ", Base.mlctobase10(mlc))