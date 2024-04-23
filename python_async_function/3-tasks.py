#!/usr/bin/env python3
"""
This module creates an asyncio.Task from a given delay function.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that will run wait_random
    with the specified max_delay.

    Args:
        max_delay (int): The maximum delay before the task completes,
        passed to wait_random.

    Returns:
        asyncio.Task: A task wrapped around the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
