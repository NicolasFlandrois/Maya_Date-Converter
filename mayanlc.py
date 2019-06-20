#!usr/bin/python3.7
# UTF8
# Date: Thu 20 Jun 2019 13:00:45 CEST 
# Author: Nicolas Flandrois

from engine import Engine

def main():
    """Main running function."""

    Engine.mlcnow()

    while True:
        responce = str(Engine.menu())
        if responce == 'q':
            # Quit program.
            break
        elif responce == '1':
            # Convert Date to MLC.  
            Engine.mlcnow()
            pass
        elif responce == '2':
            # Convert Date to MLC.  
            Engine.date2mlc()
            pass
        elif responce == '3':
            # Translate MLC to Date.
            Engine.mlc2date()
            pass
        else:
            print("We couldn't understand your choice. Please try again.")
            pass


if __name__ == '__main__':
    main()
