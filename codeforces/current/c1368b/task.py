import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

from functools import reduce
from operator import mul

def product(a):
    return reduce(mul, a, 1)


def solve(k):
    s = 'codeforces'
    n = len(s)

    f = [1] * n
    i = 0
    while product(f) < k:
        f[i % n] += 1
        i += 1

    return ''.join([s[i]*f[i] for i in range(n)])


def main():
    k = ri()
    wi(solve(k))


if __name__ == '__main__':
    main()
