import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a])); sys.stdout.write('\n')


inf = 10**10


from collections import deque


def solve(n, m, d, g, mx):
    for i in range(n):
        g[i] = sorted(g[i], key=lambda x: x[1])

    lo = 0
    hi = mx + 1
    dist_best = []
    pre_best = []

    while hi > lo + 1:
        t = (lo + hi) // 2

        dist = [inf] * n
        pre = [-1] * n
        dist[0] = 0
        q = deque()
        q.append(0)

        found = False
        while q:
            v = q.popleft()
            for w in g[v]:
                if w[1] > t:
                    break
                if dist[v] + 1 < dist[w[0]]:
                    dist[w[0]] = dist[v] + 1
                    pre[w[0]] = v
                    if w[0] == n-1 and dist[n - 1] <= d:
                        found = True
                        break
                q.append(w[0])
            if found:
                break

        if dist[n-1] <= d:
            dist_best = dist
            pre_best = pre
            hi = t
        else:
            lo = t

    if len(dist_best) == 0:
        wi(-1)
        return

    wi(dist_best[n-1])
    path = []
    p = n-1
    while p != -1:
        path.append(p+1)
        p = pre_best[p]
    path.reverse()
    wia(path)


def main():
    n, m, d = ria()
    mx = 0
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = ria()
        u -= 1
        v -= 1
        g[u].append((v, c))
        mx = max(mx, c)
    solve(n, m, d, g, mx)


class FastReader(io.IOBase):
    newlines = 0

    def __init__(self, fd, chunk_size=1024*8):
        self._fd = fd
        self._chunk_size = chunk_size
        self.buffer = io.BytesIO()

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, size=-1):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size if size == -1 else size))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()


class FastWriter(io.IOBase):

    def __init__(self, fd):
        self._fd = fd
        self.buffer = io.BytesIO()
        self.write = self.buffer.write

    def flush(self):
        os.write(self._fd, self.buffer.getvalue())
        self.buffer.truncate(0), self.buffer.seek(0)


class FastStdin(io.IOBase):
    def __init__(self, fd=0):
        self.buffer = FastReader(fd)
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


class FastStdout(io.IOBase):
    def __init__(self, fd=1):
        self.buffer = FastWriter(fd)
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.flush = self.buffer.flush


if __name__ == '__main__':
    sys.stdin = FastStdin()
    sys.stdout = FastStdout()
    main()