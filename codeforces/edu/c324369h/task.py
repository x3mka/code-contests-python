import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

def pref_sum_1d(a):
    n = len(a)
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]
    return b

def diff_1d(a):
    n = len(a)
    diffs = [0] * (n-1)
    for i in range(n-1):
        diffs[i] = a[i+1] - a[i]
    return diffs

# [lx, rx) += d,   usually a if a diffs array here
def add_in_range_1d(a, lx, rx, d):
    n = len(a)
    a[lx] += d
    if rx < n:
        a[rx] -= d

def solve(n, a, q, changes):
    b = [(a[i], i) for i in range(n)]
    b.sort(reverse=True)
    h = [0] + [x[0] for x in b]
    diffs = diff_1d(h)
    for i in range(q):
        k, x = changes[i]
        add_in_range_1d(diffs, 0, k, x)
    res = pref_sum_1d(diffs)[1:]
    for i in range(n):
        b[i] = (b[i][1], res[i])
    b.sort()
    return [x[1] for x in b]

def main():
    n = ri()
    a = ria()

    q = ri()
    changes = []
    for i in range(q):
        k, x = ria()
        changes.append((k, x))
    wia(solve(n, a, q, changes))


if __name__ == '__main__':
    main()
