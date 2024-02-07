#!/usr/bin/env python3
"""
a function that returns the log message obfuscated
"""


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    message_str = ""

    message_list = message.split(separator)[:4]

    for message in message_list:
        if message.split("=")[0] in fields:
            message_str += f"{message.split('=')[0]}={redaction}{separator}"
        else:
            message_str += f"{message}{separator}"
    return message_str
