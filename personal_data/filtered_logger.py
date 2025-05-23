#!/usr/bin/env python3
import re
"""
Write a function called filter_datum that returns the log message obfuscated
"""


def filter_datum(fields, redaction, message, separator):
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character
    is separating all fields in the log line (message)
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
