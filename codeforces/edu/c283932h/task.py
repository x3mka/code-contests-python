import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def can(x, c, nb, ns, nc, pb, ps, pc, r):
    # can get x hamburgers
    # need x * c['B'] of bread, x * c['S'] of sausage and x * c['C'] of cheese
    return max(x * c['B'] - nb, 0) * pb + max(x * c['S'] - ns, 0) * ps + max(x * c['C'] - nc, 0) * pc <= r



from collections import Counter


def solve(s, nb, ns, nc, pb, ps, pc, r):
    c = Counter(s)
    lo = 0
    hi = r + nb + ns + nc

    while hi > lo + 1:
        mid = (lo + hi) // 2
        if can(mid, c, nb, ns, nc, pb, ps, pc, r):
            lo = mid
        else:
            hi = mid
    return lo


def main():
    s = rs()
    nb, ns, nc = ria()
    pb, ps, pc = ria()
    r = ri()
    wi(solve(s, nb, ns, nc, pb, ps, pc, r))


if __name__ == '__main__':
    main()
