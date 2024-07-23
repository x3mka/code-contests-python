import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


inf = 10**18


def solve(n, a, nei):
    # If monster u is killed at time x ,
    # all its adjacent monsters v will be killed in range [1 , x — 1] U [x + 1 , upper bound ] .
    # So dp[i][j] denotes the minimum cost to kill all monsters in subtree rooted at i ,
    # where ith monster is killed at the jth second .

    m = 20
    dp = [[a[i] * (j + 1) for j in range(m)] for i in range(n)]

    par = [-1] * n
    seen = [False] * n
    q = [0]
    seen[0] = True
    seq = []

    # building toposort and parents
    while q:
        v = q.pop()
        seq.append(v)

        for w in nei[v]:
            if seen[w]:
                continue
            q.append(w)
            seen[w] = True
            par[w] = v

    # reverse toposort order make sure children are processed before parent
    for i in reversed(seq):
        if par[i] == -1:
            continue

        # dp[i][bi]=a[i]⋅bi+∑j∈Cimax1≤bj≤m,bj≠bidp[j][bj]
        aa = [inf] * m
        x = inf
        for j in range(m):
            aa[j] = min(aa[j], x)
            x = min(x, dp[i][j])
        x = inf
        for j in range(m - 1, -1, -1):
            aa[j] = min(aa[j], x)
            x = min(x, dp[i][j])

        for j in range(m):
            dp[par[i]][j] += aa[j]

    return min(dp[0])


import os
from io import IOBase, BytesIO


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")



def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        nei = [[] for i in range(n)]
        for i in range(n-1):
            l, r = ria()
            l -= 1
            r -= 1
            nei[l].append(r)
            nei[r].append(l)
        wi(solve(n, a, nei))


if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
