import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, k = ria()
    a = ria()
    mx = max(a)

    lo = mx - 1
    hi = sum(a)
    while hi > lo + 1:
        mid = (lo + hi) // 2
        cnt = 0
        c = 0

        for i in range(n):
            if c + a[i] <= mid:
                c += a[i]
            else:
                cnt += 1
                c = a[i]
        if c > 0:
            cnt += 1
        if cnt <= k:
            hi = mid
        else:
            lo = mid

    wi(hi)


if __name__ == '__main__':
    main()
