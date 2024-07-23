import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, a):
    ans = sys.maxsize
    l = 0
    cur = 0
    for r in range(n):
        cur += a[r]
        while cur - a[l] >= s:
            cur -= a[l]
            l += 1
        if cur >= s:
            ans = min(ans, r - l + 1)

    return -1 if ans == sys.maxsize else ans


def main():
    n, s = ria()
    a = ria()
    wi(solve(n, s, a))


if __name__ == '__main__':
    main()