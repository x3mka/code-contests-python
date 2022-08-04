import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')

import sys
from functools import lru_cache

V = [0]
W = [0]
dp = []

@lru_cache(maxsize=None)
def solve(v, L):
    if v == 1:
        if W[v] > L:
            return 0
        return V[v]
    p = v // 2

    res = [solve(p, L)]  # not taking v
    if L >= W[v]:
        res.append(solve(p, L - W[v]) + V[v])  # taking v
    return max(res)


def main():
    global V, W
    n = ri()
    for _ in range(n):
        vx, wx = ria()
        V.append(vx)
        W.append(wx)
    q = ri()
    for _ in range(q):
        v, L = ria()
        wi(solve(v, L))


if __name__ == '__main__':
    main()
