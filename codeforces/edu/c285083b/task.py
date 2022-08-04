import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, a):
    lo = 0
    hi = sum(a)

    while hi > lo + 1:
        t = (lo + hi) // 2

        g = 0
        cg = 0
        for i in range(n):
            if cg + a[i] <= t:
                cg += a[i]
            else:
                g += 1
                cg = a[i]
                if cg > t:
                    g = n+1
                    break
        if cg > 0:
            g += 1

        if g <= k:
            hi = t
        else:
            lo = t
    return hi


def main():
    n, k = ria()
    a = ria()
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()
