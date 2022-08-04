import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    dp = [False] * n
    dp[n-1] = True

    for i in range(n-2, -1, -1):
        if dp[i + 1]:
            if a[i] > 1:
                dp[i] = True
            else:
                dp[i] = False
        else:
            dp[i] = True


    return dp[0]


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        ws('First' if solve(n, a) else 'Second')


if __name__ == '__main__':
    main()
