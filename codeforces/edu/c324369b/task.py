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


def add_arith_in_range(a, l, r, step):
    n = len(a)
    a[l] += step
    if r < n:
        a[r] -= (r - l + 1) * step
    if r + 1 < n:
        a[r + 1] += (r - l) * step


def main():
    n = ri()
    a = [0, 0] + ria()

    diffs2 = find_diffs(find_diffs(a))

    q = ri()
    for i in range(q):
        l, r, d = ria()
        add_arith_in_range(diffs2, l-1, r, d)

    res = find_prefixes(find_prefixes(diffs2))
    wia(res[2:])


if __name__ == '__main__':
    main()
