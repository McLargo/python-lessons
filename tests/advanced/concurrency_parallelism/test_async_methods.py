import asyncio
import time

from advanced.concurrency_parallelism import (
    async_method_blocked,
    async_method_not_blocked,
)


def test_async_method_not_blocked():
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(
        asyncio.gather(
            async_method_not_blocked(),
            async_method_not_blocked(),
            async_method_not_blocked(),
        ),
    )
    non_blocked_time = time.time() - start

    # assert, total time around 1 second
    assert non_blocked_time < 1.1, f"Expected <1.1s, got {non_blocked_time}s"
    assert non_blocked_time > 1, f"Expected >1s, got {non_blocked_time}s"


def test_async_method_blocked():
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(
        asyncio.gather(
            async_method_blocked(),
            async_method_blocked(),
            async_method_blocked(),
        ),
    )
    blocked_time = time.time() - start

    # assert, total time around 3 seconds
    assert blocked_time < 3.1, f"Expected <3.1s, got {blocked_time}s"
    assert blocked_time > 3, f"Expected >3s, got {blocked_time}s"
