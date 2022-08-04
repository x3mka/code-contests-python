import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, t = ria()
    a = ria()

    lo = 0
    hi = 10**18

    while hi > lo + 1:
        mid = (lo + hi) // 2
        s = sum([mid // a[i] for i in range(n)])
        if s >= t:
            hi = mid
        else:
            lo = mid

    wi(hi)


if __name__ == '__main__':
    main()
