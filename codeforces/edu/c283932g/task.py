import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def spread(a, i, k, n):
    suf = [a[n - 1]]
    for ii in range(1, n):
        suf.append(suf[ii - 1] + a[n - ii - 1])

    lo = i
    hi = n-k+1
    to_spread = a[i] * (k - 1)

    while hi > lo + 1:
        x = (lo + hi) // 2

        can = True
        s = 0
        for j in range(n-1, x, -1):
            s += min(a[j] - a[x], a[i])
            if s >= to_spread:
                break
        if s < to_spread:
            can = False

        if can:
            lo = x
        else:
            hi = x

    x = lo
    s = suf[n-x-2]
    for j in range(n - 1, x, -1):
        m = (s - to_spread) // (j - x)
        change = min(a[i], a[j] - m)
        s -= a[j]
        to_spread -= change
        a[j] -= change

    a[x+1:] = sorted(a[x+1:])


# def can(x, k, n, a):
#     b = a.copy()
#
#
#     cnt = 0
#     for i in range(n-k+1):
#         if b[i] == 0:
#             continue
#         cnt += b[i]
#         if cnt >= x:
#             return True
#         to_spread = b[i] * (k-1)
#         spread(b, i, k, to_spread, b[i])
#         b[i] = 0
#         # b[i+1:] = sorted(b[i+1:])
#     return cnt >= x


import heapq

def compress(k, n, h):
    heapq.heapify(h)
    while len(h) > 2* k:
        a1 = heapq.heappop(h)
        a2 = heapq.heappop(h)
        heapq.heappush(h, a1 + a2)
    return h


def solve(k, n, a):
    a = sorted(a)
    cnt = 0

    for i in range(n-k+1):
        cnt += a[i]
        spread(a, i, k, n)
        a[i] = 0

    return cnt


def solve_naive(k, n, a):
    cnt = 0
    b = sorted(a.copy(), reverse=True)
    while b[k-1] > 0:
        cnt += 1
        for i in range(k):
            b[i] -= 1
        b = sorted(b, reverse=True)
    return cnt


import random


def gen():
    # k = 2
    # n = 50
    # a = [random.randrange(100) + 1 for _ in range(n)]
    # wia([k, n])
    # wia(a)
    # wi(solve(2, 50, a))
    # return

    for k in range(2, 21):
        for n in range(k, 51):
            for t in range(100):
                # a = [random.randrange(10**9) + 1] * n
                a = sorted([random.randrange(100) + 1 for _ in range(n)])
                # ac = compress(k, n, a.copy())
                # wia(a)
                # wia(ac)
                res = solve(k, n, a)
                # res21 = solve_naive(k, n, a)
                # res22 = solve_naive(k, n, ac)
                # if res21 != res22:
                #      wia([k, n])
                #      wia(a)
                #      wia(ac)
                #      wia([res21, res22])
                #      raise Exception()
            ws("Done for k={0} and n={1}".format(k, n))


def main():
    # gen()
    # return
    xx = list(map(int, sys.stdin.read().split()))
    k = xx[0]
    n = xx[1]
    a = xx[2:]
    wi(solve(k, n, a))


if __name__ == '__main__':
    main()
