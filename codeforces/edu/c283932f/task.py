import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def can(x, t, p, a):
    s = set(a[:x])
    ok = True
    j = 0
    for i in range(len(p)):
        while j < len(t) and (t[j] != p[i] or j+1 in s):
            j += 1
        if j >= len(t):
            ok = False
            break
        else:
            j += 1
    return ok


def solve(t, p, a):
    lo = 0
    hi = len(a)

    while hi > lo + 1:
        mid = (lo + hi) // 2
        if can(mid, t, p, a):
            lo = mid
        else:
            hi = mid
    return lo


def main():
    t = rs()
    p = rs()
    a = ria()
    wi(solve(t, p, a))


if __name__ == '__main__':
    main()
