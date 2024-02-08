#!/usr/bin/env python3
"""
a function that expects one string argument
and returns a salted, hashed password,
which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """encrypts password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
