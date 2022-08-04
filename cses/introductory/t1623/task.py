import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    a = ria()

    best = sum(a)

    for mask in range(0, 1 << n):
        s1 = 0
        s2 = 0
        for bit in range(n):
            if (mask & (1 << bit)) > 0:
                s1 += a[bit]
            else:
                s2 += a[bit]

        best = min(best, abs(s1 - s2))

    wi(best)


if __name__ == '__main__':
    main()
