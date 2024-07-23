import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a, b):
    c = [0] * (n + m)
    i = 0
    j = 0
    while i < n or j < m:
        if j == m or i < n and a[i] < b[j]:
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            j += 1
    return c


def main():
    n, m = ria()
    a = ria()
    b = ria()
    wia(solve(n, m, a, b))


if __name__ == '__main__':
    main()