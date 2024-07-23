import bisect
import sys
from itertools import accumulate


def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, x, a):
    pre = [0] + list(accumulate(a))

    dp = [0] * n

    for i in range(n-1, -1, -1):
        j = bisect.bisect_right(pre, pre[i] + x)
        dp[i] = j - i - 1
        if j < n:
            dp[i] += dp[j]

    return sum(dp)


def main():
    for _ in range(ri()):
        n, x = ria()
        a = ria()
        wi(solve(n, x, a))


if __name__ == '__main__':
    main()
