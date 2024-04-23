#!/usr/bin/env python3
"""
This module measures the runtime of executing
multiple async comprehensions in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel
    and measure the total runtime.

    Returns:
        float: The total time it took to run
        all async_comprehension calls concurrently.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
