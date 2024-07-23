import math
import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


sys.setrecursionlimit(1000000)


M = 10**9 + 7

N = 5000
c = [[0] * (n+1) for n in range(N+1)]
c[0][0] = 1
for n in range(N+1):
    c[n][0] = 1
    c[n][n] = 1
    for k in range(1, n):
        c[n][k] = (c[n-1][k-1] + c[n-1][k]) % M


def choose(n, k):
    if n < k:
        return 0
    return c[n][k]


def solve(n):
    ans = 0
    for k in range(n+1):  # size of a subset
        for mex in range(k+1, 2*k+2):
            picked = mex - (k + 1)
            ways = choose(min(n, mex-1), picked)

            if picked < k:
                ways *= choose(n - mex, k - picked)

            ans = (ans + ways * mex) % M

    return ans % M


def main():
    for _ in range(ri()):
        n = ri()
        wi(solve(n))


if __name__ == '__main__':
    main()
