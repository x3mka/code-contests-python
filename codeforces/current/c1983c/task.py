import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import bisect


def solve(n, a, b, c):
    tot = sum(a)
    needed = tot // 3 + (1 if tot % 3 > 0 else 0)

    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    pc = [0] * (n + 1)
    for i in range(1, n+1):
        pa[i] = pa[i - 1] + a[i - 1]
        pb[i] = pb[i - 1] + b[i - 1]
        pc[i] = pc[i - 1] + c[i - 1]

    for i in range(1, n-1):
        if pa[i] >= needed:
            j = bisect.bisect_left(pb, needed + pb[i], lo=i, hi=n)
            sb = pb[j] - pb[i]
            sc = pc[n] - pc[j]
            if sb >= needed and sc >= needed:
                return [1, i, i+1, j, j+1, n]

            j = bisect.bisect_left(pc, needed + pc[i], lo=i, hi=n)
            sc = pc[j] - pc[i]
            sb = pb[n] - pb[j]
            if sb >= needed and sc >= needed:
                return [1, i, j + 1, n, i + 1, j]

        if pb[i] >= needed:
            j = bisect.bisect_left(pa, needed + pa[i], lo=i, hi=n)
            sa = pa[j] - pa[i]
            sc = pc[n] - pc[j]
            if sa >= needed and sc >= needed:
                return [i+1, j, 1, i, j+1, n]

            j = bisect.bisect_left(pc, needed + pc[i], lo=i, hi=n)
            sc = pc[j] - pc[i]
            sa = pa[n] - pa[j]
            if sa >= needed and sc >= needed:
                return [j+1, n, 1, i, i+1, j]

        if pc[i] >= needed:
            j = bisect.bisect_left(pa, needed + pa[i], lo=i, hi=n)
            sa = pa[j] - pa[i]
            sb = pb[n] - pb[j]
            if sa >= needed and sb >= needed:
                return [i+1, j, j+1, n, 1, i]

            j = bisect.bisect_left(pb, needed + pb[i], lo=i, hi=n)
            sb = pb[j] - pb[i]
            sa = pa[n] - pa[j]
            if sa >= needed and sb >= needed:
                return [j+1, n, i+1, j, 1, i]

    return [-1]


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        c = ria()
        wia(solve(n, a, b, c))


if __name__ == '__main__':
    main()
