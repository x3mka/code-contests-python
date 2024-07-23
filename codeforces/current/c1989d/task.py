import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a, b, c):
    max_a = max(a)
    M = max_a + 1

    best = [M] * M
    for i in range(n):
        diff = a[i] - b[i]
        best[a[i]] = min(best[a[i]], diff)

    ans = [0] * M
    waste = M
    for i in range(M):
        waste = min(waste, best[i])
        if waste < M:
            ans[i] = 2 + ans[i - waste]

    res = 0
    for ci in c:
        if ci < M:
            res += ans[ci]
        else:
            v = 1 + (ci - M) // waste
            ci -= v * waste
            res += ans[ci] + 2 * v

    return res


def main():
    n, m = ria()
    a = ria()
    b = ria()
    c = ria()
    wi(solve(n, m, a, b, c))


if __name__ == '__main__':
    main()
