import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def can(x, m, n, t, z, y):
    cnt = 0
    res = []
    got = False
    for i in range(n):
        if got:
            res.append(0)
            continue
        k = x // (t[i] * z[i] + y[i])
        c = k * z[i]
        taken = k * (t[i] * z[i] + y[i])
        if taken + t[i] * z[i] <= x:
            c += z[i]
            taken += t[i] * z[i]
        else:
            c += (x - taken) // t[i]
        cnt += c
        if cnt >= m:
            got = True
            res.append(c - cnt + m)
        else:
            res.append(c)
    return got, res


def solve(m, n, t, z, y):
    lo = 0
    hi = (t[0] + y[0]) * m
    res = [0] * n
    res[0] = m

    while hi > lo + 1:
        mid = (lo + hi) // 2
        ok, mid_res = can(mid, m, n, t, z, y)
        if ok:
            hi = mid
            res = mid_res
        else:
            lo = mid
    wi(hi)
    wia(res)


def main():
    m, n = ria()
    t = []
    z = []
    y = []
    for _ in range(n):
        ti, zi, yi = ria()
        t.append(ti)
        z.append(zi)
        y.append(yi)

    solve(m, n, t, z, y)


if __name__ == '__main__':
    main()
