import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()

    m = 10**9 + 7
    dp = [0] * (n + 1)

    dp[0] = 1
    for i in range(n + 1):
        for d in range(1, 7):
            if i + d <= n:
                dp[i + d] = (dp[i + d] + dp[i]) % m

    wi(dp[n])


if __name__ == '__main__':
    main()
