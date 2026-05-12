"""Concurrency and parallelism.

This module contains examples of concurrent and parallel programming in Python.
"""

from .concurrency import (
    async_method_blocked,  # noqa: F401
    async_method_not_blocked,  # noqa: F401
    concurrent_with_thread_pool,  # noqa: F401
)
from .parallelism import (
    parallelism_with_concurrent_process_pool,  # noqa: F401
    parallelism_with_multiprocess,  # noqa: F401
)
