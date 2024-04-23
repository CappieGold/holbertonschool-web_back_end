#!/usr/bin/env python3
"""methode call methode"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of the wait_n
    coroutine and calculate the average time per call.

    Args:
        n (int): The number of times to invoke the
        wait_random coroutine within wait_n.
        max_delay (int):
        The maximum delay passed to wait_random within wait_n.

    Returns:
        float: The average time taken per call of wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
