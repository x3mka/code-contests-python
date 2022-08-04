import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    s = []
    m = 10**9+7

    for i in range(n):
        s.append(rs())

    if s[0][0] == '*':
        wi(0)
        return

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if j < n-1 and s[i][j + 1] == '.':
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % m
            if i < n-1 and s[i + 1][j] == '.':
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % m

    wi(dp[n-1][n-1])


if __name__ == '__main__':
    main()
