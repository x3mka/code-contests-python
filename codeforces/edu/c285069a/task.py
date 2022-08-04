import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from itertools import accumulate


eps = 1e-12

def solve(n, d, a):
    lo = -1
    hi = max(a) + 1
    ans = []

    while abs(hi-lo) > eps:
        t = (lo + hi) / 2

        b = [a[i] - t for i in range(n)]

        pre = [0] + list(accumulate(b))

        m = [0]
        mn = pre[0]
        for i in range(1, n+1):
            m.append(i if pre[i] < mn else m[i-1])
            mn = min(mn, pre[i])

        can = False
        for r in range(d, n+1):
            # l in range(0, r-d)
            if pre[r] >= pre[m[r-d]]:
                can = True
                ans = [m[r - d] + 1, r]
                # break

        if can:
            lo = t
        else:
            hi = t
    return ans


import random


def solve_naive(n, d, a):
    best = -1
    idx = []
    for ln in range(d, n+1):
        for i in range(n-ln+1):
            avg = sum(a[i:i+ln]) / ln
            if avg >= best:
                best = avg
                idx = [i+1, i+ln]
    return idx


def gen():
    for n in range(1, 10):
        for d in range(1, n+1):
            for t in range(100):
                a = [random.randrange(100) for _ in range(n)]
                res1 = solve_naive(n, d, a)
                res2 = solve(n, d, a)
                if res1 != res2 and sum(a[res1[0]-1:res1[1]])*(res2[1]-res2[0]) != sum(a[res2[0]-1:res2[1]])*(res1[1]-res1[0]):
                    wia([n, d])
                    wia(a)
                    wia(res1)
                    wia(res2)
                    raise Exception

def main():
    # gen()
    # return
    n, d = ria()
    a = ria()
    wia(solve(n, d, a))


if __name__ == '__main__':
    main()
