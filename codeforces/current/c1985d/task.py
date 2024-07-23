import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a):
    # too complex, one can just find row/col with max # count

    s = [[0]*(m+1) for i in range(n+1)]  # s[i][j] - number of # in 0..i-1 x 0..j-1
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if a[i-1][j-1] == '#' else 0)

    for i in range(n):
        for j in range(m):
            s1 = s[i+1][j+1]
            s2 = s[i+1][m] - s[i+1][j]
            s3 = s[n][j+1] - s[i][j+1]
            s4 = s[n][m] - s[i][m] - s[n][j] + s[i][j]
            if s1 == s2 == s3 == s4:
                return [i+1, j+1]
    return []


def main():
    for _ in range(ri()):
        n, m = ria()
        a = [""] * n
        for i in range(n):
            a[i] = rs()
        wia(solve(n, m, a))


if __name__ == '__main__':
    main()
