#!/usr/bin/env python3
"""
This module defines a coroutine that uses async
comprehension to collect values from an async generator.
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Asynchronously collects 10 random numbers using
    an async comprehension over async_generator.

    Returns:
        list: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
