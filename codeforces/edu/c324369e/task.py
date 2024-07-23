import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def find_diffs(a):
    n = len(a)
    diffs = [0] * (n-1)
    for i in range(n-1):
        diffs[i] = a[i+1] - a[i]
    return diffs


def find_prefixes(a):
    n = len(a)
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]
    return b


# [lx, rx) += d,   usually a if a diffs array here
def add_in_range_1d(a, lx, rx, d):
    n = len(a)
    a[lx] += d
    if rx < n:
        a[rx] -= d

def main():
    n, m, k = ri()
    a = [0] + ria()

    diffs = find_diffs(a)

    for i in range(m):
        l, r, d = ria()
        add_in_range_1d(diffs, l-1, r, d)

    res = find_prefixes(diffs)
    wia(res[1:])


if __name__ == '__main__':
    main()
