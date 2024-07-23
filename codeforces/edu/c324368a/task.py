import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def main():
    n, m = ria()
    a = [[0]*m for _ in range(n)]

    for i in range(n):
        a[i] = ria()

    b = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + a[i-1][j-1]

    q = ri()
    for i in range(q):
        lx, ly, rx, ry = ria()
        wi(b[rx][ry]-b[rx][ly-1]-b[lx-1][ry]+b[lx-1][ly-1])


if __name__ == '__main__':
    main()
