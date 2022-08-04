import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter
from itertools import permutations
from random import randrange


def solve_naive(n, a):
    ans = 0
    for b in permutations(a):
        best = n
        for i in range(n):
            for j in range(i + 1, n):
                if b[i] == b[j]:
                    best = min(best, j - i - 1)
        ans = max(ans, best)
    return ans


def solve(n, a):
    c = Counter(a)
    cnt = c.most_common()[0][1]
    rep = sum([1 for k, v in c.items() if v == cnt])
    return (n - rep) // (cnt - 1) - 1

    c = Counter(a)
    b = c.most_common()
    m = len(b)

    lo = n
    idx = 0
    prev = {}
    bb = b.copy()
    while len(bb) > 0:
        for i in range(len(bb)):
            k, v = bb[i]
            if k in prev:
                lo = min(lo, idx - prev[k] - 1)
            prev[k] = idx
            bb[i] = (k, v - 1)
            idx += 1
        while len(bb) > 0 and bb[-1][1] == 0:
            bb.pop()

    hi = n

    while hi > lo + 1:
        mid = (lo + hi) // 2

        can = True
        s = set([i for i in range(n)])

        for i in range(m):
            if not can:
                break
            idx = next(iter(s))
            for j in range(b[i][1]):
                if idx >= n:
                    can = False
                    break
                s.remove(idx)
                idx += mid + 1

        if can:
            lo = mid
        else:
            hi = mid

    return lo


def gen():
    for n in range(2, 9):
        for k in range(1, n + 1):
            for t in range(30):
                a = [randrange(k) + 1 for _ in range(n)]
                if Counter(a).most_common(1)[0][1] < 2:
                    continue
                res1 = solve(n, a)
                res2 = solve_naive(n, a)
                if res1 != res2:
                    wi(n)
                    wia([res1, res2])
                    wia(a)
                    return


def main():
    # gen()
    # return

    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))
        # wi(solve_naive(n, a))


if __name__ == '__main__':
    main()
