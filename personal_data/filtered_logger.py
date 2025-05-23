#!/usr/bin/env python3
import re
"""
Write a function called filter_datum that returns the log message obfuscated
"""


def filter_datum(fields, redaction, message, separator):
    """ task 0 """
    pattern = r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
