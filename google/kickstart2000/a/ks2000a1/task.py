import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from itertools import accumulate
from bisect import bisect


def solve(n, b, a):
    a = sorted(a)
    pre = list(accumulate(a))
    return bisect(pre, b)


def main():
    for t in range(ri()):
        n, b = ria()
        a = ria()
        ws("Case #{}: {}".format(t+1, solve(n, b, a)))


if __name__ == '__main__':
    main()
