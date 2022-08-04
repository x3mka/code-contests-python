import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


import heapq
from collections import deque


def solve(n, s, g, e):
    parent = [-1] * n
    cnt = [0] * n

    # top_sorted = []
    #
    # taken = [False] * n
    # taken[0] = True
    #
    # q = deque([0])
    # while q:
    #     v = q.popleft()
    #     top_sorted.append(v)
    #     for w in g[v]:
    #         if not taken[w[0]]:
    #             taken[w[0]] = True
    #             q.append(w[0])
    #             parent[w[0]] = v
    #
    #
    # for v in top_sorted[::-1]:
    #     if len(g[v]) == 1:
    #         cnt[v] = 1
    #         if parent[v] >= 0:
    #             cnt[parent[v]] += 1
    #     else:
    #         if parent[v] >= 0:
    #             cnt[parent[v]] += cnt[v]


    @bootstrap
    def dfs(v, p=-1):
        for w in g[v]:
            if w[0] == p:
                continue
            parent[w[0]] = v
            yield dfs(w[0], v)
            cnt[v] += cnt[w[0]]
        if len(g[v]) == 1:
            cnt[v] += 1
        yield

    dfs(0)

    ss = 0
    q = []
    for u, v, w in e:
        x = cnt[u] if parent[u] == v else cnt[v]
        ss += w * x

        ww = w
        while True:
            delta = x * (ww - ww // 2)
            if delta > 0:
                q.append(delta)
                ww //= 2
            else:
                break

    ans = 0
    q.sort()

    while ss > s:
        ss -= q[-1]
        q.pop()
        ans += 1

    return ans


def main():
    for _ in range(ri()):
        n, s = ria()
        g = [[] for i in range(n)]
        e = []
        for i in range(n-1):
            u, v, w = ria()
            u -= 1
            v -= 1
            g[u].append((v, w))
            g[v].append((u, w))
            e.append((u, v, w))

        wi(solve(n, s, g, e))



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

