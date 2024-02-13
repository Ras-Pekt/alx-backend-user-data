#!/usr/bin/env python3
"""Basic Auth module for the API"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic Auth class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """
        Return None if:
            authorization_header is None
            authorization_header is not a string
            authorization_header does not start with Basic
        Return the value after Basic
        """
        if authorization_header is None or \
            not isinstance(authorization_header, str) or \
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """
        Return None if:
            base64_authorization_header is None
            base64_authorization_header is not a string
            base64_authorization_header is not a valid Base64
        Return the decoded value as UTF8 string
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header,
                validate=True
            ).decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Return None, None if decoded_base64_authorization_header:
            is None,
            is not a string,
            does not contain ':'.
        Return the user email and the user password
        """
        if decoded_base64_authorization_header is None or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """
        Return None if:
            user_email is None or not a string,
            user_pwd is None or not a string,
            the database (file) does not contain any User instance with email equal to user_email - you should use the class method search of the User to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.
            user_pwd is not the password of the User instance found - you must use the method is_valid_password of User
        Return the User instance
        """
        pass