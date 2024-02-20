#!/usr/bin/env python3
"""
a method that takes in a password string arguments
and returns bytes
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    returns a string representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        takes mandatory email and password
        and return a User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(
                email=email,
                hashed_password=_hash_password(password)
            )

    def valid_login(self, email: str, password: str) -> bool:
        """validates login details"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"),
                user.hashed_password
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """returns a user's session_id"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user_id=user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns User associated with session_id"""
        if session_id:
            try:
                return self._db.find_user_by(session_id=session_id)
            except Exception:
                return None
        return None

    def destroy_session(self, user_id: str):
        """destroys a session associated with user_id"""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            return None
