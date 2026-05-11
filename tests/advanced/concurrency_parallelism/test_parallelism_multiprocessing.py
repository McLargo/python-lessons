from advanced.concurrency_parallelism.utils import PRIMES

from advanced.concurrency_parallelism import parallelism_with_multiprocess


def test_parallelism_with_multiprocess():
    results = parallelism_with_multiprocess()

    # assert we got results for all primes
    assert len(results) == len(PRIMES)

    # assert results are expected
    expected_prime_results = {r[0]: r[1] for r in results}

    assert expected_prime_results[999999999999988] is False
    assert expected_prime_results[999999999999989] is True
    assert expected_prime_results[999999999999990] is False

    # assert multiple processes were used (different PIDs)
    pids = set(r[2] for r in results)
    assert len(pids) > 1, (
        f"Expected multiple processes, but only got {len(pids)}"
    )
