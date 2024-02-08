#!/usr/bin/env python3
"""
a function that expects one string argument
and returns a salted, hashed password,
which is a byte string
"""
from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """encrypts password using bcrypt"""
    return hashpw(password.encode('utf-8'), gensalt())
