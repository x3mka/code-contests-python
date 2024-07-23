import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(a, n, l, r):
    ans = 0

    start, end = 0, 0
    s = 0
    while start < n:
        while end < n and s < l:
            s += a[end]
            end += 1
        if l <= s <= r:
            ans += 1
            start = end
            s = 0
        else:
            s -= a[start]
            start += 1

    return ans


def main():
    for _ in range(ri()):
        n, l, r = ria()
        a = ria()
        wi(solve(a, n, l, r))


if __name__ == '__main__':
    main()
