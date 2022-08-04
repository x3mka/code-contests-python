import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

import math
eps = 1e-9

def solve(c):
    lo = 0
    hi = c

    f = lambda x: x*x + math.sqrt(x) - c

    while abs(hi-lo) > eps:
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return hi


def main():
    c = float(rs())
    wi(solve(c))


if __name__ == '__main__':
    main()
