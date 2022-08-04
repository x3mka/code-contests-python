import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

import math
eps = 1e-7

def solve(n, k, a):
    lo = 0
    hi = max(a)

    while abs(hi-lo) > eps:
        mid = (lo + hi) / 2
        if sum([math.floor(ai / mid) for ai in a]) < k:
            hi = mid
        else:
            lo = mid
    return hi


def main():
    n, k = ria()
    a = []
    for _ in range(n):
        a.append(ri())
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()
