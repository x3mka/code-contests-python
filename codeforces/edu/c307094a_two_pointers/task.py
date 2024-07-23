import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, p, a):
    s = sum(a)
    rounds = p // s
    p %= s

    if p == 0:
        return [1, rounds * n]

    b = a + a
    m = n * 2

    best_start = 0
    best = m
    l = 0
    cur = 0
    for r in range(m):
        cur += b[r]
        while cur - b[l] >= p:
            cur -= b[l]
            l += 1
        if cur >= p:
            if r - l + 1 < best:
                best = r - l + 1
                best_start = l

    return [best_start + 1, rounds * n + best]


def main():
    n, p = ria()
    a = ria()
    wia(solve(n, p, a))


if __name__ == '__main__':
    main()