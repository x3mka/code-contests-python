import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def count(x, n):
    ans = 0
    for d in range(1, n+1):
        c = x // d
        if x % d == 0:
            c -= 1
        if c <= 0:
            break
        ans += min(c, n)
    return ans


def solve(n, k):
    lo = 1
    hi = n * n + 1

    while hi > lo + 1:
        x = (lo + hi) // 2

        if count(x, n) < k:
            lo = x
        else:
            hi = x
    return lo


def gen():
    for n in range(1, 10):
        for k in range(1, n*n+1):
            a = []
            for i in range(1, n+1):
                for j in range(1, n+1):
                    a.append(i * j)
            a = sorted(a)
            if solve(n, k) != a[k-1]:
                wia([n, k, solve(n, k), a[k-1]])
                raise Exception


def main():
    # gen()
    # return
    n, k = ria()
    wi(solve(n, k))


if __name__ == '__main__':
    main()
