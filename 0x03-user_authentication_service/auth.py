#!/usr/bin/env python3
"""
a method that takes in a password string arguments
and returns bytes
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
