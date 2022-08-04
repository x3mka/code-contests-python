import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

from collections import Counter
from itertools import groupby
from math import gcd


def solve(n, k, s):
    sd = sorted(Counter(s).values(), reverse=True)

    ans = 0
    for m in range(1, n+1):
        d = gcd(m, k)
        d1 = m // d
        if sum([x // d1 for x in sd]) >= d:
            ans = m

    return ans


def main():
    for _ in range(ri()):
        n, k = ria()
        s = rs()
        wi(solve(n, k, s))


if __name__ == '__main__':
    main()
