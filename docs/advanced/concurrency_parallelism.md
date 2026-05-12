# Concurrency and parallelism

These concepts are related, but not the same. Concurrency is the ability of a
program to execute multiple task by interleaving them, while parallelism is the
ability of a program to execute multiple tasks at the same time on multiple CPU
cores.

Note that concurrency and parallelism are not just for python, but for any
programming language that allows the execution of code to be non-blocking by the
CPU.

## Concurrency

In python, concurrency is achieved with several ways, such as with threads or
with the `asyncio` library.

### Threads

Threads are a way to achieve concurrency in python. They are excellent for
I/O-bound tasks, but they are not recommended for CPU-bound tasks due to the
Global Interpreter Lock (GIL) in Python preventing true parallelism. GIL
restrict execution of one thread at a time, even on multi-core processors. All
threads are executed in the **same process** and share the same memory space, so
context switching between threads is faster than between processes.

::: src.advanced.concurrency_parallelism.concurrent_with_thread_pool

Aside what we already mentioned about the GIL, threads can also lead to race
conditions and deadlocks if not used properly.

Race conditions happens when two or more threads access to shared data and try
to update. It can affect to the expected output, and will be hard to debug. You
can use locks to prevent threads to access shared data until the lock is
released.

Deadlocks happens when two or more threads are waiting for each other to release
a resource, such as a lock. This can lead to a situation where none of the
threads can proceed, and the program will be stuck.

### Asyncio

`asyncio` is a python native library, which provides a way to write concurrent
code using the `async` and `await` keywords.

`async` keyword is used to define a function as asynchronous, which means that
it can be paused and resumed at a later time. This is handled automatically by
the library, which allows the CPU to switch between different tasks while
waiting for a task to complete.

`await` keyword is used to pause the execution of an asynchronous function until
task is completed. This allows the CPU to switch to other tasks while waiting
for the task to complete, which can improve the performance of the program.

::: src.advanced.concurrency_parallelism.async_method_not_blocked

`await/async` should not be used in a context where the CPU cannot do other
things while waiting for a task to complete, as it will not improve the
performance of the program. Those words are not a magic solution to make your
code faster. Always check with 3party libraries if they are compatible with
`asyncio` before using it.

::: src.advanced.concurrency_parallelism.async_method_blocked

## Parallelism

In python, parallelism is achieved with with different libraries. Parallelism
can be useful for CPU-bound tasks that require a lot of computational power.

### multiprocessing

The `multiprocessing` library allows you to create multiple processes that can
run in parallel on multiple CPU cores.

::: src.advanced.concurrency_parallelism.parallelism_with_multiprocess

### concurrent.futures

The `concurrent.futures` library provides a high-level interface for
asynchronously executing callables. It provides a `ProcessPoolExecutor` class
that allows you to create a pool of processes that can run in parallel on
multiple CPU cores. This can be useful for CPU-bound tasks that require a lot of
computational power.

::: src.advanced.concurrency_parallelism.parallelism_with_concurrent_process_pool

## Performance consideration and real world usage

Concurrency and parallelism are tools that will help to improve your program.
But needs to be used properly.

- For CPU-bound tasks that require a lot of computational power, use
  multiprocessing/Process Pool. Threading/async won't help due to the GIL.
- For I/O-bound tasks, such as network request, read/write database or file
  operations, use `asyncio` for the best performance, then threads. Multiprocess
  here will be overkill and inefficient.
- Overhead (extra time and resources to manage threads and processes) is bigger
  in multiprocessing than in threads or asyncio. Even starting up new process
  takes more time than starting a new thread.
- Multiprocessing requires that all data passed must be picklable (serializable),
  which can be a limitation for some use cases.
