import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


M = 10**9 + 7

def log(n):
    ans = 0
    while n > 1:
        ans += 1
        n //= 2
    return ans


def cn2(n):
    return (n * (n + 1) // 2) % M


N = 61
# dp[i][k] - # of k beautiful segments in range [0, 2**i - 1]
dp = [[1]*N for _ in range(N)]
for k in range(N):
    dp[0][k] = 1

for i in range(1, N):
    for j in range(1, N):
        if i == j:
            dp[i][j] = cn2(1 << j)
        elif j > i:
            dp[i][j] = dp[i][j - 1]
        elif i == j + 1:
            dp[i][j] = cn2((1 << i) - 1)
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % M


def solve(n, k):
    l = log(n)
    if l == 0 or k == 0:
        return 1
    elif 1 << l == n:
        return dp[l][k]
    elif l <= k:
        return cn2(n)
    else:
        return (dp[l][k] + solve(n - (1 << l), k - 1)) % M


def main():
    for _ in range(ri()):
        n, k = ria()
        wi(solve(n, k))


if __name__ == '__main__':
    main()
