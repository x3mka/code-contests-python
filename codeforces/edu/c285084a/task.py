import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def count(x, p):
    ans = 0
    for i in range(len(p)):
        if x <= p[i][0]:
            continue
        ans += min(p[i][1], x) - p[i][0]
    return ans


def solve(n, k, p):
    lo = -10**12
    hi = 10**12

    while hi > lo + 1:
        x = (lo + hi) // 2

        if count(x, p) <= k:
            lo = x
        else:
            hi = x
    return lo


def main():
    n, k = ria()
    p = []
    for _ in range(n):
        p.append(ria())
        p[-1][1] += 1
    wi(solve(n, k, p))


if __name__ == '__main__':
    main()
