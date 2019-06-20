#!usr/bin/python3.7
# UTF8
# Date: Thu 20 Jun 2019 13:00:45 CEST 
# Author: Nicolas Flandrois

import os 
import platform
import datetime
from datecompute import Convert
from basecompute import Base
from longcount import Longcount

def clean():
    """This function will clear the terminal's screen. The command is 
    automaticaly detected according to the system OS you run it."""
    print("(Appuyez sur Entrer pour continuer)")
    input()
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear") #This command will work on Linux and OSx systems.

def main():
    """Main running function."""

    d = datetime.datetime.now()
    t = d.timetuple()

    ed_display = d.strftime('%A, %Y %B %d. %H:%M:%S')
    print('Today\'s date : ', ed_display)
    Longcount.mayanlc_display(Longcount.mayanlc(Convert.nowdate()))



if __name__ == '__main__':
    main()