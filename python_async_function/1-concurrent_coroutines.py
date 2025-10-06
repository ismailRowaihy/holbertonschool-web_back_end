#!/usr/bin/env python3
"""this module with afunction that sleeps with a random value """


import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """a function that sleeps with random value"""
    list_Delays = []
    asyncio.get_running_loop()
    for i in range(n):
        num = await wait_random(max_delay)
        list_Delays.append(num)

    return sorted(list_Delays)
