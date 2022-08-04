import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def find_lower(n, a, x):
    l = -1
    r = n
    while r > l + 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return l


def solve(n, a, x):
    i = find_lower(n, a, x)
    return i >= 0 and a[i] == x


def main():
    n, k = ria()
    a = ria()
    kk = ria()
    for i in range(k):
        ws('YES' if solve(n, a, kk[i]) else 'NO')


if __name__ == '__main__':
    main()
