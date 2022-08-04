import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
def flush(): sys.stdout.flush()


import math


class SparseTable:

    def __init__(self, data):
        self._n = n = len(data)
        self._k = k = int(math.log2(n))+1
        self.data = data
        self.st = [[0] * k for _ in range(n)]

        for i in range(n):
            self.st[i][0] = data[i]

        j = 1
        while (1 << j) <= n:
            i = 0
            while (i + (1 << j) - 1) < n:
                if (self.st[i][j - 1] >
                        self.st[i + (1 << (j - 1))][j - 1]):
                    self.st[i][j] = self.st[i][j - 1]
                else:
                    self.st[i][j] = self.st[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self, l, r):
        j = int(math.log2(r - l + 1))
        if self.st[l][j] >= self.st[r - (1 << j) + 1][j]:
            return self.st[l][j]
        else:
            return self.st[r - (1 << j) + 1][j]

    def __repr__(self):
        return "SparseTable({0})".format(self.st)


def main():
    n, m = ria()
    h = ria()
    st = SparseTable(h)
    cnt = 0
    for _ in range(m):
        a, b = ria()
        if abs(a-b) > 1:
            if st.query(min(a, b), max(a, b)-2) <= h[a-1]:
                cnt += 1
        else:
            cnt += 1
    wi(cnt)


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
