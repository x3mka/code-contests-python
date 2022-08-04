import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    res = []

    while n > 0:
        s = set(a[:n])
        mex = 0
        while mex < n and mex in s:
            mex += 1

        if mex == n:
            a[n-1] = mex
            res.append(n)
            n -= 1
        else:
            res.append(mex + 1)
            a[mex] = mex

    wi(len(res))
    wia(res)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
