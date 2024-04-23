#!/usr/bin/env python3
"""async methode"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay
    between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int, optional):
        The maximum delay time in seconds. Defaults to 10.

    Returns:
        float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
