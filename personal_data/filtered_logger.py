#!/usr/bin/env python3
import re
""" Task 0 """


def filter_datum(fields, redaction, message, separator):
    """ Task 0 """
    patt = rf'({"|".join(map(re.escape, fields))})=[^{re.escape(separator)}]*'
    return re.sub(patt, lambda m: f"{m.group(1)}={redaction}", message)
