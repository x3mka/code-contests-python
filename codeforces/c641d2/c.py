from math import sqrt
from itertools import takewhile


def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def odd_numbers(start=3):
    while True: yield start; start += 2


def primes():
    yield 2
    d = [2]
    gen = odd_numbers()
    while True:
        c = next(gen)
        if all([c % p for p in d]):
            yield c
            d.append(c)


def multiplicity(n, p):
    res = 0
    while n % p == 0:
        res += 1
        n //= p
    return res


def main():
    n = ri()
    a = ria()

    max_a = int(sqrt(max(a)))+1
    cached_primes = list(takewhile(lambda p: p <= max_a, primes()))

    def pp(r, p):
        degrees = []
        deg0_count = 0
        for i in range(n):
            deg = multiplicity(a[i], p)
            degrees.append(deg)
            a[i] //= p**deg
            if deg == 0:
                deg0_count += 1
            if deg0_count == 2:
                break
        deg = sorted(degrees)[1]
        return r * p**deg

    res = 1

    for p in cached_primes:
        res = pp(res, p)

    left_pps = [ai for ai in a if ai > 1]
    for p in left_pps:
        res = pp(res, p)

    print(res)


if __name__ == '__main__':
    main()
