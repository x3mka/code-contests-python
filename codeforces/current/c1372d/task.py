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

    b = a[::2] + a[1::2]
    b += b

    k = (n + 1) // 2
    s = sum(b[:k])
    best = s
    for r in range(k, 2*n):
        s += b[r] - b[r-k]
        best = max(best, s)

    wi(best)


if __name__ == '__main__':
    main()
