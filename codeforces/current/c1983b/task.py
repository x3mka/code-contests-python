import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a, b):
    sa_rows = [0] * n
    sa_cols = [0] * m
    sb_rows = [0] * n
    sb_cols = [0] * m

    for i in range(n):
        for j in range(m):
            sa_rows[i] += a[i][j]
            sa_cols[j] += a[i][j]
            sb_rows[i] += b[i][j]
            sb_cols[j] += b[i][j]

    r = sum([1 for i in range(n) if sa_rows[i] % 3 != sb_rows[i] % 3])
    c = sum([1 for j in range(m) if sa_cols[j] % 3 != sb_cols[j] % 3])

    return "YES" if c + r == 0 else "NO"


def main():
    for _ in range(ri()):
        n, m = ria()

        a = [[0]*m for _ in range(n)]
        for i in range(n):
            a[i] = list(map(int, list(rs())))

        b = [[0] * m for _ in range(n)]
        for i in range(n):
            b[i] = list(map(int, list(rs())))

        ws(solve(n, m, a, b))


if __name__ == '__main__':
    main()
