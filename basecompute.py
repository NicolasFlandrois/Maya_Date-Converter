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
        # Returns a Tuple (a, b) ('a' (Tiple[0]) will be compute for the next digit, 
        # 'b' (Tiple[1]) is the reminder)

    def baseNto10(n_input, n_base): 
        """This function will compute from Base-N to Base-10"""
        a = n_input*n_base
    #   b = n_input%n_base #?????
        return a # , b # Returns a Tuple (a, b)

# Class Translation():
# Using the following computation.
# 9.12.2.0.16 (Long Count)
#   9   × 144000    = 1296000
#   12  × 7200  = 86400
#   2   × 360   = 720
#   0   × 20    = 0
#   16  × 1 = 16
#   Total days  = 1383136

#TEST
# print("base10toN")
# print("Base 20: ", Base.base10toN(50, 20))
# print("Base 18: ", Base.base10toN(50, 18))
# print("baseNto10")
# print("Base 20: ", Base.baseNto10(60, 20))
# print("Base 18: ", Base.baseNto10(40, 18))
