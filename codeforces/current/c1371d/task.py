import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k):
    a = [[0]*n for _ in range(n)]

    cnt = min(k, n)
    for i in range(cnt):
        a[i][i] = 1

    if k > cnt:
        dr = 1
        for d in range(1, 2*n):
            done = False
            if dr == 1:
                dn = n - (d+1) // 2
                for r in range(dn):
                    a[r][r+(d+1)//2] = 1
                    cnt += 1
                    if cnt == k:
                        done = True
                        break
                dr = -1
            else:
                for r in range(d//2):
                    a[n - d//2 + r][r] = 1
                    cnt += 1
                    if cnt == k:
                        done = True
                        break
                dr = 1
            if done:
                break

    rr = [sum(a[i]) for i in range(n)]
    r_min = min(rr)
    r_max = max(rr)

    cc = [0]*n
    for r in range(n):
        for j in range(n):
            cc[j] += a[r][j]
    c_min = min(cc)
    c_max = max(cc)

    f = (r_max - r_min) ** 2 + (c_max - c_min) ** 2
    wi(f)
    for i in range(n):
        ws(''.join([str(x) for x in a[i]]))


def main():
    for _ in range(ri()):
        n, k = ria()
        solve(n, k)


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
