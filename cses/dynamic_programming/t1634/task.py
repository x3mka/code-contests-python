import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, x = ria()
    a = ria()

    dp = [x + 1] * (x + 1)

    dp[0] = 0
    for i in range(x + 1):
        for ai in a:
            if i + ai <= x:
                dp[i + ai] = min(dp[i + ai], dp[i] + 1)

    wi(dp[x] if dp[x] != x + 1 else -1)


if __name__ == '__main__':
    main()
