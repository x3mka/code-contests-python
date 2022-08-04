import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def primes_up_to(n):
    pp = [2]
    for i in range(3, n+1):
        pi = 0
        is_prime = True
        while pi < len(pp) and pp[pi] * pp[pi] <= i:
            if i % pp[pi] == 0:
                is_prime = False
                break
            pi += 1
        if is_prime:
            pp.append(i)
    return pp


# primes = primes_up_to(10**5)

def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True


def solve(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 1:
        return True

    k = 0
    m = n
    while m % 2 == 0:
        k += 1
        m //= 2

    if m == 1:
        return False

    # m > 1
    if k > 1:
        return True  # div by m

    # k == 1,   n = 2 * odds
    # is_prime = True
    # pi = 0
    # while pi < len(primes) and primes[pi] * primes[pi] <= m:
    #     if m % primes[pi] == 0:
    #         is_prime = False
    #         break

    return not is_prime(m)


def main():
    for _ in range(ri()):
        n = ri()
        ws("Ashishgup" if solve(n) else "FastestFinger")


if __name__ == '__main__':
    main()
