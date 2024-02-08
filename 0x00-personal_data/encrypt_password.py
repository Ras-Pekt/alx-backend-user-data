#!/usr/bin/env python3
"""
a function that expects one string argument
and returns a salted, hashed password,
which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """encrypts password using bcrypt"""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password
