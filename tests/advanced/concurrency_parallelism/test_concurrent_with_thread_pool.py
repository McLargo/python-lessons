from advanced.concurrency_parallelism.utils import PRIMES

from advanced.concurrency_parallelism import concurrent_with_thread_pool


def test_concurrent_with_thread_pool():
    results = concurrent_with_thread_pool()

    # assert we got results for all primes
    assert len(results) == len(PRIMES)

    # assert results are expected
    expected_prime_results = {r[0]: r[1] for r in results}

    assert expected_prime_results[999999999999988] is False
    assert expected_prime_results[999999999999989] is True
    assert expected_prime_results[999999999999990] is False

    # assert single process was used (same PID)
    pids = set(r[2] for r in results)
    assert len(pids) == 1, f"Expected a single process, but got {len(pids)}"
