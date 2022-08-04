import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for si in str(i):
            if dp[i] == 0:
                dp[i] = dp[i - int(si)] + 1
            else:
                dp[i] = min(dp[i], dp[i - int(si)] + 1)

    wi(dp[n])


if __name__ == '__main__':
    main()
