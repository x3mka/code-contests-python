import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, K, z, a):
    # (i, j, k) , at i-th now, made j turns left and k = 1 if last turn is left
    dp = [[[0]*2 for j in range(z + 1)] for i in range(n)]
    dp[0][0][0] = a[0]

    for j in range(z + 1):
        for i in range(n):
            for k in range(2):
                if i < n - 1:
                    dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][k] + a[i + 1]) # move right
                if i > 0 and j < z and k == 0:
                    dp[i - 1][j + 1][1] = max(dp[i - 1][j + 1][1], dp[i][j][0] + a[i - 1]) # move left

    ans = 0
    for j in range(z + 1):
        i = K - 2 * j
        if i < 0:
            continue
        ans = max(ans, dp[i][j][0], dp[i][j][1])

    return ans


def main():
    for _ in range(ri()):
        n, k, z = ria()
        a = ria()
        wi(solve(n, k, z, a))


if __name__ == '__main__':
    main()
