import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def pre_calc():
    mx = 16
    dp = [[[0] * (mx + 1) for j in range(mx + 1)] for i in range(mx + 1)]
    # center shifted (to make all coords >= 0)
    dp[0][mx // 2][mx // 2] = 1

    res = []

    for d in range(1, mx + 1):
        for i in range(1, mx):
            for j in range(1, mx):
                dp[d][i][j] = dp[d - 1][i][j + 1] + \
                              dp[d - 1][i][j - 1] + \
                              dp[d - 1][i - 1][j] + \
                              dp[d - 1][i + 1][j] + \
                              dp[d - 1][i + 1][j - 1] + \
                              dp[d - 1][i - 1][j + 1]
        # we need to store this to results b/c this value will change for the next d's
        res.append(dp[d][mx // 2][mx // 2])

    return res


def main():
    ans = pre_calc()
    for _ in range(ri()):
        n = ri()
        wi(ans[n-1])


if __name__ == '__main__':
    main()
