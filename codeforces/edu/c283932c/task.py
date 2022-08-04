import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def can(t, n, x, y):
    if x > y:
        x, y = y, x
    return t // x + (t - x) // y >= n


def solve(n, x, y):
    lo = 0
    hi = max(x, y) * n

    while hi > lo + 1:
        mid = (lo + hi) // 2
        if can(mid, n, x, y):
            hi = mid
        else:
            lo = mid
    return hi


def main():
    n, x, y = ria()
    wi(solve(n, x, y))


if __name__ == '__main__':
    main()
