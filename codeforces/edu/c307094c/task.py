import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, d):
    a = [0] * (n - 1)
    for i in range(n-1):
        a[i] = d[i+1] - d[i]
    ans = 0
    l = 0
    cur = 0
    for r in range(0, n-1):
        cur += a[r]
        while cur - a[l] > s:
            cur -= a[l]
            l += 1
        if cur > s:
            ans += l + 1

    return ans


def main():
    n, r = ria()
    d = ria()
    wi(solve(n, r, d))


if __name__ == '__main__':
    main()