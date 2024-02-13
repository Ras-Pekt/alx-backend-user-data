#!/usr/bin/env python3
"""Auth module for the API"""
from typing import List, TypeVar
from flask import request
import fnmatch


class Auth:
    """Authentication Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        return True if authentication is required, False otherwise.
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        normalized_path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(normalized_path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        return Authorization header value.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return Current user.
        """
        return None