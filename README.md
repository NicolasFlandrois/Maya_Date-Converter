# maya_date
## Python script to compute, convert, and translate dates into Mayan Calendar Long Count date.
==============

### Mayan Calendar Project :
	* Generate Mayan Long Count Calendar according to current time. Changing reference date.
	* Convert an input date (from gregorian ISO-8601 calendar) to Long Count.
	* Translate a Long Count Input, into a Gregorian date (ISO-8601 calendar).

### Tzolkin Ha'ab Project :
	* Same 2 generator, convertor, translator, for Tzolkin and Ha'ab Mayan Calendar. Which is more difficult, as they are cycles, and don't refer to a year.
		- Generator for Today's date (now)
		- Convert a Date to Tzolkin/Ha'ab
		- Translate from Tzolkin/Ha'ab to Date (If possible)

--------------

By Launching the program in Python (Python 3.7 and above), the current Date and Long Count are displaid. Then, by pressing 'Enter', the menu is displaid:

+ Long Count Now (Today's date) Automatic
+ Convert a Date to Long Count
+ Translate a Long Count to Date
+ Quit

--------------
## Remaining issues and To Do List:

### Long Count:
- [ ] Due to Datetime Module's limitations During conversion, Years < 1000 cannot be converted
	* A try/except loop verifying the exception, and raising a text explaining, should suffice
- [ ] Due to Datetime Module's limitations During translation, Years < 1000 cannot be translated
	* A try/except loop verifying the exception, and raising a text explaining, should suffice
- [ ] How this issue of time before Year 1000 could be solved? How can we compute those Ancient time?

### Tzolkin
- [ ] Create a convertor engine (Date > Tzolkin)
- [ ] Create a Translator "reverse engine" (Tzolkin > Date) - If Possible, The year might be tricky to translate.
- [ ] Auto Convert, For date now (Today's date)
- [ ] Display & Integration in main program

### Ha'ab
- [ ] Create a convertor engine (Date > Ha'ab)
- [ ] Create a Translator "reverse engine" (Ha'ab > Date) - If Possible, The year might be tricky to translate.
- [ ] Auto Convert, For date now (Today's date)
- [ ] Display & Integration in main program