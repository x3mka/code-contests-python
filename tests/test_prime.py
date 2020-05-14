from lib.ntheory.prime import primes_up_to
import timeit


def test_primes():
    start_time = timeit.default_timer()
    primes_up_to(10000000)
    print(timeit.default_timer() - start_time)


def test_primes_cached():
    data = primes_up_to(10000000)
    cached_gen = (y for y in data)
    start_time = timeit.default_timer()
    primes_up_to(10000000, cached_gen)
    print(timeit.default_timer() - start_time)










