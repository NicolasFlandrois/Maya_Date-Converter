#!/usr/bin/python3.7
# UTF8
# Date: Thu 20 Jun 2019 13:00:45 CEST 
# Author: Nicolas Flandrois

import os 
import platform
import datetime
from datecompute import Convert
from basecompute import Base
from lccompute import Longcount


class Engine(object):
    """Engine will use necessary function from other class, and display a
    user friendly view."""

    def clean():
        """
        This function will clear the terminal's screen. The command is 
        automaticaly detected according to the system OS you run it.
        Compatible with Windows, OSx, and Linux.
        """
        os.system("cls" if platform.system() == "Windows" else "clear")

    def ask_integer(message:str, range, error_message:str = ""):
        """
        This function's purpose is to ask and verify an Integer.
        """
        var = None
        while True:
            try:
                var = int(input(message))
                if var in range:
                    return var
                    raise
                    
            except KeyboardInterrupt:
                break
                
            except:
                print(error_message)

    def menu():
        Engine.clean()
        print("Mayan Long Count Calendar.\n")
        Engine.mlcnow()
        print('\n')
        while True:
            responce = input("Do you want to do some other MLC operation?\n\
press:\n\
        1 : Compute Today\'s Mayan Long Count.\n\
        2 : To Convert a Date into a Mayan Long Count.\n\
        3 : To Translate a Mayan Long Count into a Date.\n\
        R : Return to main menu.\n\
        Q : To Quit.\n\n")
            Engine.clean()

            try:
                if responce.strip().lower() in ['r', 'q', '1', '2', '3']:
                    if responce.strip().lower() == 'r':
                        # Return to main menu.
                        continue
                    elif responce.strip().lower() == 'q':
                        # Quit program.
                        break
                    elif responce.strip().lower() == '1':
                        Engine.clean()
                        # Convert Date to MLC. 
                        Engine.mlcnow()
                        print('\n')
                    elif responce.strip().lower() == '2':
                        Engine.clean()
                        # Convert Date to MLC.  
                        Engine.date2mlc()
                        print('\n')
                    elif responce.strip().lower() == '3':
                        Engine.clean()
                        # Translate MLC to Date.
                        Engine.mlc2date()
                        print('\n')
                    else:
                        raise
                else:
                    raise          
            except:
                print("We couldn't understand your choice. Please try again.")

    def mlcnow():
        """Display & Compute Today's date into MLC"""
        d = datetime.datetime.now()
        t = d.timetuple()

        ed_display = d.strftime('%A, %Y %B %d. %H:%M:%S')

        print('Today\'s date :                 ', ed_display)
        print('\nToday\'s Mayan Long Count :     ',
              Longcount.mayanlc_display(Longcount.mayanlc(Convert.nowdate())))

    def date2mlc():
        """Display & Convert Date to MLC."""
        dlist = []
        dlist.append(Engine.ask_integer("Year? (YYYY format) ",
                                     range(-10000000, 10000000)))
        # Issue here, Years <1000 raise an Error Message. 
        # Due to datetime modules' limitations.
        # Create here a Try/Except Methode to rule out this kind of error.
        dlist.append(Engine.ask_integer("Month? (from 01 to 12) ",
            range(1, 13)))
        dlist.append(Engine.ask_integer("Day of the month? (from 01 to 31) ",
                                 range(1, 32)))

        dstring = " ".join([str(i) for i in dlist])
        d = datetime.datetime.strptime(dstring, '%Y %m %d') 
        date_display = d.strftime('%A, %Y %B %d')

        Engine.clean()
        print(f'{date_display}, corrresponds to the Mayan Long Count:\n\n',
            Longcount.mayanlc_display(Longcount.mayanlc(
                Convert.inputdate(dlist[0], dlist[1], dlist[2]))))

    def mlc2date():
        """Display & Translate MLC to Date"""
        date = Convert.date_translator(
            Base.mlctobase10(Longcount.mayanlc_input()))

        date_display = date.strftime('%A, %Y %B %d')
        
        print(f'\nThis Mayan Long Count corrresponds to the date:\n\n\
               {date_display}.')
