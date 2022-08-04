def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res


import math
primes = prime_list(int(math.sqrt(10**9))+1)


def factorize(n):
    global primes
    i = 0
    d = {}
    while n > 1 and i < len(primes) and primes[i] * primes[i] <= n:
        if n % primes[i] == 0:
            d[primes[i]] = 0
            while n % primes[i] == 0:
                d[primes[i]] += 1
                n //= primes[i]
        i += 1
    if n > 1:
        d[n] = 1
    return d


from functools  import reduce
def divisors(n):
    factors = [(x[0], x[1]) for x in factorize(n).items()]
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def solve(n, k):
    if k >= n:
        return 1

    divs = sorted(list(divisors(n)), reverse=True)
    for d in range(len(divs)):
        if divs[d] <= k:
            return n // divs[d]

    return n


def main():
    for _ in range(ri()):
        n, k = ria()
        print(solve(n, k))


if __name__ == '__main__':
    main()
