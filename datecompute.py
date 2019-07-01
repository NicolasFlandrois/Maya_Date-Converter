#!/usr/bin/python3
# UTF8
# Date: Mon 27 May 2019 22:30:04 CEST
# Author: Nicolas Flandrois

import datetime


class Convert(object):
    """Convert will regroup functions managing dates convertion."""

    def nowdate():
        """Date now"""
        return datetime.date.today()

    def inputdate(year, month, day):
        """Formating the date into a computable format."""
        return datetime.date(year, month, day)

    def convertor(datedata):
        """Issuing the date argument (datedata) as a decimal integer ready to
        be converted into Mayan count bases (Base-20 and Base-18)"""
        ref_a = datetime.date(1970, 1, 1)
        # Choosen as ref point, as this date is Unix Time = 0
        ref_b = 1856305  # Long Count Base(20): 0.0.0.0.0.12.17.16.7.5
        # which can be translated into base(20) = CHG75
        # Decimal (base 10) value of maya long count's ref point
        delta = datedata - ref_a
        # Decimal value of maya long count for today
        # Then convert this decimal into base(20)
        return ref_b + delta.days

    def date_translator(lcdecimal: int):
        """Translator from a Long Count Decimal Integer (lcdecimal:int),
        this function will translate it into a date object."""
        ref_a = datetime.date(1970, 1, 1)
        # Choosen as ref point, as this date is Unix Time = 0
        ref_b = 1856305  # Long Count Base(20): 0.0.0.0.0.12.17.16.7.5
        # which can be translated into base(20) = CHG75
        # Decimal (base 10) value of maya long count's ref point
        delta = datetime.timedelta(days=(lcdecimal - ref_b))
        return ref_a + delta
