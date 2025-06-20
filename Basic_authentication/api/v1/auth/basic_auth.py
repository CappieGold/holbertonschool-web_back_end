#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication
        Args:
            authorization_header: the Authorization header value
        Returns:
            The Base64 part of the Authorization header, or None if invalid
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Return everything after "Basic " (after the space)
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string
        Args:
            base64_authorization_header: the Base64 string to decode
        Returns:
            The decoded value as UTF8 string, or None if invalid
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 to bytes, then decode bytes to UTF-8 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user email and password from decoded Base64 string
        Args:
            decoded_base64_authorization_header: decoded Base64 string
        Returns:
            Tuple of (email, password) or (None, None) if invalid
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split on first occurrence of ':'
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password
        Args:
            user_email: the user's email
            user_pwd: the user's password
        Returns:
            User instance if credentials are valid, None otherwise
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            # Search for users with the given email
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        # Get the first user (should be unique by email)
        user = users[0]

        # Verify the password
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request
        Args:
            request: Flask request object
        Returns:
            User instance if authentication is successful, None otherwise
        """
        # Step 1: Get authorization header
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Step 2: Extract Base64 part
        base64_header = self.extract_base64_authorization_header(auth_header)
        if base64_header is None:
            return None

        # Step 3: Decode Base64
        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None

        # Step 4: Extract user credentials
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if user_email is None or user_pwd is None:
            return None

        # Step 5: Get user object from credentials
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
