#!/usr/bin/env python3
"""
a function that returns the log message obfuscated
"""
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record_dict = record.__dict__
        for field in self.fields:
            record_dict[field] = self.filter_datum(
                # record_dict.get(field, ""), self.REDACTION, record.getMessage(), self.SEPARATOR
                self.fields, self.REDACTION, record_dict.get(field, ""), self.SEPARATOR
            )
        return super().format(record)

    def filter_datum(self, fields: List, redaction: str, message: str, separator: str) -> str:
        """returns the log message obfuscated"""
        message_str = ""

        message_list = message.split(separator)[:4]

        for message in message_list:
            if message.split("=")[0] in fields:
                message_str += f"{message.split('=')[0]}={redaction}{separator}"
            else:
                message_str += f"{message}{separator}"
        return message_str
