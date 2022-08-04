import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a):
    cnt = 0
    for i in range(n - 1):
        if a[i][m-1] != 'D':
            cnt += 1
    for j in range(m - 1):
        if a[n - 1][j] != 'R':
            cnt += 1

    return cnt


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for i in range(n):
            a.append(rs())
        wi(solve(n, m, a))


if __name__ == '__main__':
    main()
