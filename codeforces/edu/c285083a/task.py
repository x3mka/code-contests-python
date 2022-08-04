import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


eps = 1e-6


def intersect(s1, s2):
    return max(s1[0], s2[0]), min(s1[1], s2[1])


def solve(n, x, v):
    lo = 0
    hi = (max(x) - min(x)) / min(v)

    while abs(hi - lo) > eps:
        t = (lo + hi) / 2

        seg = (x[0] - v[0] * t, x[0] + v[0] * t)
        for i in range(1, n):
            seg = intersect(seg, (x[i] - v[i] * t, x[i] + v[i] * t))
            if seg[1] <= seg[0]:
                break
        if seg[1] - seg[0] > 0:
            hi = t
        else:
            lo = t
    return (lo + hi) / 2


def main():
    n = ri()
    x = []
    v = []
    for _ in range(n):
        xi, vi = ria()
        x.append(xi)
        v.append(vi)
    wi(solve(n, x, v))


if __name__ == '__main__':
    main()
