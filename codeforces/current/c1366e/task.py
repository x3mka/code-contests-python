import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


MOD = 998244353


def solve(n, m, a, b):
    a.reverse()
    b.reverse()

    ad = {}
    for i in range(n):
        if a[i] not in ad:
            ad[a[i]] = []
        ad[a[i]].append(i)

    cnt = 1

    if b[0] not in ad:
        return 0
    x = ad[b[0]][0]
    min_ax = min(a[:x+1])
    if min_ax < b[0]:
        return 0

    for i in range(1, m):
        if b[i] not in ad:
            return 0
        k = 0
        yy = ad[b[i]]
        while k < len(yy) and yy[k] < x:
            k += 1
        if k > len(yy)-1:
            return 0
        y = yy[k]

        min_xy = min(a[x:y+1])
        if min_xy < b[i]:
            return 0

        mid = x + 1
        while mid <= y and a[mid] >= b[i-1]:
            mid += 1

        cnt = (cnt * (mid - x)) % MOD
        x = y

    min_last = min(a[x:])
    if min_last < b[m-1]:
        return 0

    return cnt


def main():
    n, m = ria()
    a = ria()
    b = ria()
    wi(solve(n, m, a, b))


if __name__ == '__main__':
    main()
