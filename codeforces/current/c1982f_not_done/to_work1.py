# https://codeforces.com/contest/1982/submission/267419552

import bisect
import heapq
import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def f(u, v):
    return u << 24 ^ v

def get_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

def add(i, x):
    while i < len(tree):
        tree[i] += x
        i += i & -i

t = int(input())
ans = []
inf = pow(10, 9) + 1
for _ in range(t):
    n = int(input())
    a = [-inf] + list(map(int, input().split())) + [inf]
    q = int(input())
    q0 = [0] * (q << 1)
    x = [0] * (n + q + 2)
    for i in range(n + 2):
        x[i] = f(a[i] + inf, i)
    for i in range(q):
        pos, val = map(int, input().split())
        x[i + n + 2] = f(val + inf, pos)
        q0[i << 1], q0[i << 1 ^ 1] = pos, val + inf
    mi, ma = [], []
    tree = [0] * (n + q + 5)
    x.sort()
    for i in range(1, n + 1):
        a[i] = bisect.bisect_left(x, f(a[i] + inf, i))
        tree[a[i]] += 1
    for i in range(1, len(tree)):
        j = i + (i & -i)
        if j < len(tree):
            tree[j] += tree[i]
    for i in range(1, n + 1):
        if a[i - 1] > a[i] < a[i + 1]:
            mi.append(f(a[i], i))
        elif a[i - 1] < a[i] > a[i + 1]:
            ma.append(-f(a[i], i))
    heapq.heapify(mi)
    heapq.heapify(ma)
    ans0 = ["-1 -1" for _ in range(q + 1)]
    if mi:
        l, r = get_sum(mi[0] >> 24), get_sum(-ma[0] >> 24)
        ans0[0] = " ".join(map(str, (l, r)))
    for i in range(q):
        pos, val = q0[i << 1], q0[i << 1 ^ 1]
        add(a[pos], -1)
        a[pos] = bisect.bisect_left(x, f(val, pos))
        for j in range(max(pos - 1, 1), min(pos + 2, n + 1)):
            if a[j - 1] > a[j] < a[j + 1]:
                heapq.heappush(mi, f(a[j], j))
            elif a[j - 1] < a[j] > a[j + 1]:
                heapq.heappush(ma, -f(a[j], j))
        add(a[pos], 1)
        while mi:
            u, j = mi[0] >> 24, mi[0] & 0xffffff
            if a[j - 1] > a[j] == u < a[j + 1]:
                break
            heapq.heappop(mi)
        while ma:
            u, j = -ma[0] >> 24, -ma[0] & 0xffffff
            if a[j - 1] < a[j] == u > a[j + 1]:
                break
            heapq.heappop(ma)
        if mi:
            l, r = get_sum(mi[0] >> 24), get_sum(-ma[0] >> 24)
            ans0[i + 1] = " ".join(map(str, (l, r)))
    ans.append("\n".join(ans0))
sys.stdout.write("\n".join(ans))