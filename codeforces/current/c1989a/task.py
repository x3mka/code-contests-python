import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, c):
    for i in range(n):
        x, y = c[i]
        if y >= -1:
            ws("YES")
        else:
            ws("NO")


def main():
    n = ri()
    c = [[] for _ in range(n)]
    for i in range(n):
        c[i] = ria()
    solve(n, c)


if __name__ == '__main__':
    main()
