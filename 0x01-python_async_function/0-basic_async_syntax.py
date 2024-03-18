#!/usr/bin/env python3
"""
module doc
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    """
    r = random.uniform(0, max_delay)
    return await asyncio.sleep(r, r)
