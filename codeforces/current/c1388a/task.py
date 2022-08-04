import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def least_prime_factor(n):
    """O(n*log(log(n))) complexity and O(n) memory"""
    """Useful when n less than 10^7, otherwise memory errors"""
    lp = [0] * (n + 1)
    lp[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            for j in range(2 * i, n + 1, i):
                if lp[j] == 0:
                    lp[j] = i
    return lp


def main():
    # N = 200000
    # primes = least_prime_factor(N)
    # almost_primes = []
    # for i in range(1, N + 1):
    #     q = primes[i]
    #     p = i // q
    #     if p > 1 and q > 1 and p != q and primes[q] == q and primes[p] == p:
    #         almost_primes.append(i)

    s = {6, 10, 14}
    ss = sum(s)
    for _ in range(ri()):
        n = ri()
        if n <= ss:
            ws('NO')
        else:
            ws('YES')
            rem = n - ss
            if rem in s:
                wia([6, 10, 15] + [rem - 1])
            else:
                wia(list(s) + [rem])


if __name__ == '__main__':
    main()
