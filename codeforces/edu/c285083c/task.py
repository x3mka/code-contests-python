import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, a):
    lo = 1
    hi = max(a) - min(a) + 1

    while hi > lo + 1:
        t = (lo + hi) // 2

        cnt = 0
        prev = -10**10
        for i in range(n):
            if a[i] - prev >= t:
                cnt += 1
                prev = a[i]

        if cnt >= k:
            lo = t
        else:
            hi = t
    return lo


def main():
    n, k = ria()
    a = ria()
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()
