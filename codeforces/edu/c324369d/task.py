import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def pref_sum_1d(a):
    n = len(a)
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]
    return b

def diff_1d(a):
    n = len(a)
    diffs = [0] * (n-1)
    for i in range(n-1):
        diffs[i] = a[i+1] - a[i]
    return diffs


# [lx, rx) += d,   usually a if a diffs array here
def add_in_range_1d(a, lx, rx, d):
    n = len(a)
    a[lx] += d
    if rx < n:
        a[rx] -= d


# Solution for O(n): https://codeforces.com/blog/entry/88291?locale=ru
# Editorial: https://codeforces.com/blog/entry/88248
def solve(n, a):
    ans = 0
    c = [0] * (n + 1)
    # diff = [0] * n

    for i in range(n):
        # c = pref_sum_1d(diff)
        # c[i] = c[i-1] + diff[i] if i > 0 else 0
        extra = max(0, a[i] - 1 - c[i])
        ans += extra
        c[i] = max(c[i], a[i] - 1)

        # we make starting jumps to i+2, i+3, i+a[i], so should add +1 on range [i+2, i+a[i]+1)
        for j in range(2, min(a[i]+1, n-i)):
            c[i+j] += 1

        c[i+1] += c[i] - a[i] + 1
        # if i + 1 < n:
        #     add_in_range_1d(diff, i+1, i+a[i], 1)

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


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


# usage
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
