import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, x = ria()
    a = ria()

    ans = 0
    s = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s > x:
            s -= a[l]
            l += 1
        if s == x:
            ans += 1
    wi(ans)


if __name__ == '__main__':
    main()
