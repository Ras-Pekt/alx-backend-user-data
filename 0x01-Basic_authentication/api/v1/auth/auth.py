#!/usr/bin/env python3
"""Auth module for the API"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    template for all authentication system to be implemented
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles paths that require authorization"""
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path = f"{path}/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """validates requests"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        return None
