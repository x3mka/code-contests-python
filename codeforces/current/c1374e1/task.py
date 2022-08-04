import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, t, a, b):
    if a.count(1) < k or b.count(1) < k:
        return -1

    like_ab = sorted([i for i in range(n) if a[i] == 1 and b[i] == 1], key=lambda x: t[x])
    like_a = sorted([i for i in range(n) if a[i] == 1 and b[i] == 0], key=lambda x: t[x])
    like_b = sorted([i for i in range(n) if b[i] == 1 and a[i] == 0], key=lambda x: t[x])

    n_ab = len(like_ab)
    n_a = min(len(like_a), len(like_b))

    pre_ab = [0]
    for i in range(1, n_ab+1):
        pre_ab.append(pre_ab[i-1] + t[like_ab[i-1]])

    pre = [0]
    for i in range(1, n_a+1):
        pre.append(pre[i-1] + t[like_a[i-1]] + t[like_b[i-1]])

    ans = sum(t)
    for x in range(n_ab + 1):
        if n_a >= k - x >= 0:
            ans = min(ans, pre_ab[x] + pre[k-x])

    return ans


def main():
    n, k = ria()
    t = []
    a = []
    b = []
    for _ in range(n):
        ti, ai, bi = ria()
        t.append(ti)
        a.append(ai)
        b.append(bi)
    wi(solve(n, k, t, a, b))



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

