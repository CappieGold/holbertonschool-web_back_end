#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


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
