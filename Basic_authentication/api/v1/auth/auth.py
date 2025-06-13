#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication
        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication
        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True
        
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        
        # Normalize path by ensuring it ends with /
        normalized_path = path if path.endswith('/') else path + '/'
        
        # Check if normalized path is in excluded_paths
        if normalized_path in excluded_paths:
            return False
        
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            None for now (will be implemented later)
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request
        Args:
            request: Flask request object
        Returns:
            None for now (will be implemented later)
        """
        return None
