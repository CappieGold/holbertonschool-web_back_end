#!/usr/bin/env python3
"""
This module provides functionality for securely hashing passwords using bcrypt.

It defines two main functions:
    - `hash_password`: to securely hash a plaintext password.
    - `is_valid`: to verify a password against a previously hashed one.

The `bcrypt` library is used to ensure strong password security, with
automatic salt generation to protect against rainbow table attacks.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and a randomly generated salt.

    This function takes a plaintext password, encodes it to UTF-8,
    and applies bcrypt's hashing algorithm. A new salt is generated
    automatically for each call.

    Args:
        password (str): The plaintext password to be hashed.

    Returns:
        bytes: A salted and hashed password, ready to be stored securely.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a previously hashed password.

    This function checks whether the provided plaintext password
    matches the stored bcrypt hash.

    Args:
        hashed_password (bytes): The previously stored bcrypt hash.
        password (str): The plaintext password to verify.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


if __name__ == "__main__":
    """
    Main file

    Demonstrates the usage of hash_password and is_valid functions
    with a sample password.
    """
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
