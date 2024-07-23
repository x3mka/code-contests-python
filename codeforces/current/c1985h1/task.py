import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solve(n, m, a):
    r_touch = [m] * n
    c_touch = [n] * m

    for i in range(n):
        for j in range(m):
            if not a[i][j]:
                continue

            c_size = 0
            r = set()
            c = set()
            q = [(i, j)]
            a[i][j] = False
            while len(q) > 0:
                x, y = q.pop()
                c_size += 1
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny]:
                        q.append((nx, ny))
                        a[nx][ny] = False
                r.add(x)
                c.add(y)
                r_touch[x] -= 1
                c_touch[y] -= 1

            for x in range(max(0, min(r) - 1), min(n, max(r) + 2)):
                r_touch[x] += c_size
            for y in range(max(0, min(c) - 1), min(m, max(c) + 2)):
                c_touch[y] += c_size

    return max(max(r_touch), max(c_touch))


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
        n, m = ria()

        a = [[] for i in range(n)]
        for i in range(n):
            a[i] = [c == "#" for c in rs()]
        wi(solve(n, m, a))

        # wi(solve1(n, m, a))


if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
