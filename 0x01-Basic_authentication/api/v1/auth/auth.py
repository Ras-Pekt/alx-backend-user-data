#!/usr/bin/env python3
"""Auth module for the API"""
from flask import request
import fnmatch
from typing import List, TypeVar


class Auth:
    """
    template for all authentication system to be implemented
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles paths that require authorization"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths or \
            path[:-1] in excluded_paths or \
                f"{path}/" in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if fnmatch(path, excluded_path):
                return False

    def authorization_header(self, request=None) -> str:
        """validates requests"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        return None
