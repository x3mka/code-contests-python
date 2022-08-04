import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def find_upper(n, a, x):
    l = -1
    r = n
    while r > l + 1:
        m = (l + r) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return r


def main():
    n, k = ria()
    a = ria()
    kk = ria()
    for i in range(k):
        wi(find_upper(n, a, kk[i]) + 1)


if __name__ == '__main__':
    main()
