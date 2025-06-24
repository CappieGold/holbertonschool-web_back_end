#!/usr/bin/env python3
"""
Authentication service module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
