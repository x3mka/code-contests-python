import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
def flush(): sys.stdout.flush()


def solve(k, a, b):
    n = len(a)
    m = len(b)
    # dp[i, j] - same concept as for LCS with k=1, just one state transition happens only if there are common >= k chars
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            x = 0
            while x < min(i, j) and a[i-x-1] == b[j-x-1]:
                x += 1
            if x >= k:
                dp[i][j] = dp[i-x][j-x] + x
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


def main():
    while True:
        k = ri()
        if k == 0:
            return
        a = rs()
        b = rs()
        wi(solve(k, a, b))


if __name__ == '__main__':

    main()
