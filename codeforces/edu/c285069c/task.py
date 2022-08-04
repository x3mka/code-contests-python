import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


eps = 1e-6

from itertools import accumulate


def solve(n, k, a, b):
    lo = 0
    hi = sum(a) + 1

    while abs(hi-lo) > eps:
        t = (lo + hi) / 2

        c = sorted([a[i] - t * b[i] for i in range(n)], reverse=True)

        pre = [0] + list(accumulate(c))

        m = [0]
        mn = pre[0]
        for i in range(1, n+1):
            m.append(i if pre[i] < mn else m[i-1])
            mn = min(mn, pre[i])

        can = False
        for r in range(k, n+1):
            if pre[r] >= pre[m[r-k]]:
                can = True
                break

        if can:
            lo = t
        else:
            hi = t
    return (hi + lo) / 2


def main():
    n, k = ria()
    a = []
    b = []
    for _ in range(n):
        ai, bi = ria()
        a.append(ai)
        b.append(bi)
    wi(solve(n, k, a, b))


if __name__ == '__main__':
    main()
