import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def count(x, n, a, b):
    ans = 0
    for i in range(n):
        if a[i] + b[0] >= x:
            break

        lo = 0
        hi = n
        while hi > lo + 1:
            mid = (hi + lo) // 2
            if a[i] + b[mid] < x:
                lo = mid
            else:
                hi = mid

        ans += lo + 1
    return ans


def solve(n, k, a, b):
    a = sorted(a)
    b = sorted(b)
    lo = min(a) + min(b)
    hi = max(a) + max(b) + 1

    while hi > lo + 1:
        x = (lo + hi) // 2

        if count(x, n, a, b) < k:
            lo = x
        else:
            hi = x
    return lo


def main():
    n, k = ria()
    a = ria()
    b = ria()
    wi(solve(n, k, a, b))


if __name__ == '__main__':
    main()
