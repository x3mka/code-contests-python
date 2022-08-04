import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, s):
    d = (min(n, m) + 1) // 2
    dp = [[1] * m for i in range(n)]  # size of max rhombus starting at (i, j)

    for i in range(n-3, -1, -1):
        for j in range(1, m - 1):
            if s[i][j] != s[i+1][j-1] or s[i][j] != s[i+1][j+1] or s[i][j] != s[i+1][j] or s[i][j] != s[i+2][j]:
                continue
            dp[i][j] = max(dp[i][j], 1 + min(dp[i+1][j-1], dp[i+1][j+1], dp[i+2][j]))

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += dp[i][j]
    return ans


def main():

    n, m = ria()
    s = []
    for i in range(n):
        s.append(rs())
    wi(solve(n, m, s))


if __name__ == '__main__':
    main()
