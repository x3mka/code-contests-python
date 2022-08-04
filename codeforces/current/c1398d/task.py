import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(r, g, b, ra, ga, ba):
    ra.sort(reverse=True)
    ga.sort(reverse=True)
    ba.sort(reverse=True)

    dp = [[[0] * (b + 1) for j in range(g + 1)] for i in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + ra[i] * ga[j])
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + ra[i] * ba[k])
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + ga[j] * ba[k])

    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                ans = max(ans, dp[i][j][k])

    return ans


def main():
    r, g, b = ria()
    ra = ria()
    ga = ria()
    ba = ria()
    wi(solve(r, g, b, ra, ga, ba))


if __name__ == '__main__':
    main()
