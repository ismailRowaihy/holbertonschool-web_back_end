#!/usr/bin/env python3
"""this module with afunction that sleeps with a loop """


import asyncio
from typing import Generator 
import random


async def async_generator () -> Generator[int, None, None]:
    """a function that sleeps with loop"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)

