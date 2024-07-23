import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def diff_1d(a):
    n = len(a)
    diffs = [0] * (n-1)
    for i in range(n-1):
        diffs[i] = a[i+1] - a[i]
    return diffs


def pref_1d(a):
    n = len(a)
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]
    return b


def diffs_2d(a):
    n = len(a)
    m = len(a[0])
    diffs = [[0] * (m - 1) for _ in range(n - 1)]
    for i in range(n-1):
        for j in range(m-1):
            diffs[i][j] = a[i+1][j+1] - a[i][j+1] - a[i+1][j] + a[i][j]
    return diffs


def pref_2d(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            b[i+1][j+1] = b[i][j+1] + b[i+1][j] - b[i][j] + a[i][j]
    return b


# [lx, rx) * [ly, ry) += d
def add_in_range_2d(a, lx, rx, ly, ry, d):
    n = len(a)
    m = len(a[0])
    a[lx][ly] += d
    if ry < m:
        a[lx][ry] -= d
    if rx < n:
        a[rx][ly] -= d
    if rx < n and ry < m:
        a[rx][ry] += d


def main():
    n, m = ria()
    a = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        a[i] = [0] + ria()

    diffs = diffs_2d(a)

    q = ri()
    for i in range(q):
        lx, ly, rx, ry, d = ria()
        add_in_range_2d(diffs, lx-1, rx, ly-1, ry, d)

    res = pref_2d(diffs)
    for i in range(n):
        wia(res[i+1][1:])


if __name__ == '__main__':
    main()
