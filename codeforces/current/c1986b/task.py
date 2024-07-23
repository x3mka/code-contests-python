import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def solve(n, m, a):
    stable = False
    while not stable:
        stable = True
        for i in range(n):
            for j in range(m):
                v = a[i][j]
                good = True
                max_nei = -sys.maxsize+1
                for k in range(4):
                    if 0 <= i+di[k] < n and 0 <= j+dj[k] < m:
                        max_nei = max(max_nei, a[i+di[k]][j+dj[k]])
                        if v <= a[i+di[k]][j+dj[k]]:
                            good = False
                if good:
                    a[i][j] -= (a[i][j] - max_nei)
                    stable = False

    for i in range(n):
        wia(a[i])


def main():
    for _ in range(ri()):
        n, m = ria()
        a = [[] * m for _ in range(n)]
        for i in range(n):
            a[i] = ria()
        solve(n, m, a)


if __name__ == '__main__':
    main()
