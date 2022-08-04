import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')




from collections import deque


def k_independent_set(n, k):
    color = [-1] * n
    q = deque()
    q.append((0, 0))
    color[0] = 0

    while q:
        v, c = q.popleft()
        for w in g[v]:
            if color[w] == -1:
                color[w] = 1 - c
                q.append((w, 1 - c))

    c0 = [i + 1 for i in range(n) if color[i] == 0]
    c1 = [i + 1 for i in range(n) if color[i] == 1]
    if len(c0) >= (k+1)//2:
        return 1, c0[:(k+1)//2]
    else:
        return 1, c1[:(k+1)//2]


def find_cycle(n):
    prev = [-1] * n
    t = [-1] * n

    q = deque()
    q.append(0)
    t[0] = 0

    while q:
        v = q.popleft()

        for w in g[v]:
            if t[w] != -1:
                if t[w] >= t[v]:
                    # cycle found starting in w and ending in v
                    s = w
                    e = v
                    p1 = [s]
                    p2 = [e]
                    while s != e:
                        if t[s] >= t[e]:
                            s = prev[s]
                            p1.append(s)
                        else:
                            e = prev[e]
                            p2.append(e)
                    p1.pop()
                    return p1 + list(reversed(p2))
            else:
                t[w] = t[v] + 1
                prev[w] = v
                q.append(w)


def k_cycle(n, k):
    c = find_cycle(n)

    cn = len(c)
    cg = {}
    for i in range(cn):
        cg[c[i]] = [c[(i-1+cn) % cn], c[(i+1) % cn]]

    while len(c) > k:
        found = False
        for i in range(cn):
            cv = c[i]
            cutting_edges = [w for w in g[cv] if w in cg and w != cg[cv][0] and w != cg[cv][1]]
            if len(cutting_edges) == 0:
                continue
            w = cutting_edges[0]
            new_c = []
            for j in range(i, i + cn):
                new_c.append(c[j % cn])
                if c[j % cn] == w:
                    break
            c = new_c
            found = True
            break
        if not found:
            break

    if len(c) <= k:
        return 2, [i+1 for i in c]

    res = [ci+1 for i, ci in enumerate(c) if i % 2 == 0]
    return 1, res[:min((k+1)//2, len(res))]


def solve(n, m, k):
    is_tree = m == n-1  # граф связный по условию
    if is_tree:
        return k_independent_set(n, k)
    else:
        return k_cycle(n, k)


g = []

def main():
    global g
    n, m, k = ria()
    g = [[] for _ in range(n)]
    for _ in range(m):
        v, w = ria()
        g[v-1].append(w-1)
        g[w-1].append(v-1)

    t, res = solve(n, m, k)
    wi(t)
    if t == 2:
        wi(len(res))
    wia(res)


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

