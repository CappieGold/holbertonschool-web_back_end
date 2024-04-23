#!/usr/bin/env python3
"""
Module to execute multiple tasks concurrently and gather their results.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n tasks that wait for a random time up to max_delay seconds.
    Returns a list of the waited times as soon as each task completes.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.
    
    Returns:
        List[float]: List of delays from the completed tasks, in the order they completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
