import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a):
    if n == 1 and m == 1:
        wi(-1)
        return

    b = [[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            b[i][j] = (a[i][j] % (n * m)) + 1

    for i in range(n):
        wia(b[i])


def main():
    for _ in range(ri()):
        n, m = ria()
        a = [[] for i in range(n)]
        for i in range(n):
            a[i] = ria()
        solve(n, m, a)


if __name__ == '__main__':
    main()
