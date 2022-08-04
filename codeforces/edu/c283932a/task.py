import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(w, h, n):
    lo = 0
    hi = max(w, h) * n
    while hi > lo + 1:
        mid = (lo + hi) // 2
        good = (mid // w) * (mid // h) >= n
        if good:
            hi = mid
        else:
            lo = mid
    return hi


def main():
    w, h, n = ria()
    wi(solve(w, h, n))


if __name__ == '__main__':
    main()
