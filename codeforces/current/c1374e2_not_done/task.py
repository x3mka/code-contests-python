import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, m, k, t, a, b):
    if a.count(1) < k or b.count(1) < k:
        wi(-1)
        return
    # if n == 243:
    #     wia([a.count(1), b.count(1)])
    #     return
    if m == n:
        wi(sum(t))
        wia([i+1 for i in range(n)])
        return

    like_ab = sorted([i for i in range(n) if a[i] == 1 and b[i] == 1], key=lambda x: t[x])
    like_a = sorted([i for i in range(n) if a[i] == 1 and b[i] == 0], key=lambda x: t[x])
    like_b = sorted([i for i in range(n) if b[i] == 1 and a[i] == 0], key=lambda x: t[x])
    like_none = sorted([i for i in range(n) if a[i] == 0 and b[i] == 0], key=lambda x: t[x])

    ans = 0
    taken = 0
    satisfied = 0
    s = []

    i = 0
    j = 0
    inf = 10 ** 10

    while satisfied < k:
        if i < len(like_ab):
            t1 = t[like_ab[i]]
            t2 = t[like_a[j]] + t[like_b[j]] if j < len(like_a) and m - taken > 1 else inf
            if t1 <= t2:
                s.append(like_ab[i] + 1)
                ans += t1
                i += 1
                taken += 1
                satisfied += 1
            else:
                s.append(like_a[j] + 1)
                s.append(like_b[j] + 1)
                ans += t2
                j += 1
                taken += 2
                satisfied += 1
        else:
            if j < len(like_a):
                s.append(like_a[j] + 1)
                s.append(like_b[j] + 1)
                ans += t[like_a[j]] + t[like_b[j]]
                j += 1
                taken += 2
                satisfied += 1
                if taken > m:
                    wi(-1)
                    return

    ss = set(s)
    tt = sorted([(t[i], i) for i in range(n)])
    i = 0
    while taken < m:
        if tt[i][1]+1 not in ss:
            s.append(tt[i][1] + 1)
            ans += tt[i][0]
            taken += 1
        i += 1

    wi(ans)
    wia(s)


def main():
    n, m, k = ria()
    t = []
    a = []
    b = []
    for _ in range(n):
        ti, ai, bi = ria()
        t.append(ti)
        a.append(ai)
        b.append(bi)
    solve(n, m, k, t, a, b)



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

