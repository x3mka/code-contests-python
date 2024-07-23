import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def s1(n, a):
    a = [0] + a
    l = [0 for _ in range(n + 1)]  # index of left el bigger than at i
    r = [0 for _ in range(n + 1)]  # index of right el bigger than at i
    ans = 0

    for i in range(1, n + 1):
        l[i] = i - 1
        while l[i] and a[i] >= a[l[i]]:
            l[i] = l[l[i]]
    for i in reversed(range(1, n + 1)):
        r[i] = i + 1
        while r[i] <= n and a[i] > a[r[i]]:
            r[i] = r[r[i]]
        ans += a[i] * (i - l[i]) * (r[i] - i)
    return ans


def solve(n, a):
    return s1(n, a) + s1(n, [-x for x in a])


def s11(n, a):
    left_bigger_or_equal_idx = [-1] * n
    min_stack = []
    for i in range(n):
        while min_stack and a[min_stack[-1]] < a[i]:
            min_stack.pop()
        if min_stack:
            left_bigger_or_equal_idx[i] = min_stack[-1]
        min_stack.append(i)

    right_bigger_idx = [n] * n
    min_stack = []
    for i in range(n-1, -1, -1):
        while min_stack and a[min_stack[-1]] <= a[i]:
            min_stack.pop()
        if min_stack:
            right_bigger_idx[i] = min_stack[-1]
        min_stack.append(i)

    ans = 0
    for i in range(n):
        ans += a[i] * (i - left_bigger_or_equal_idx[i]) * (right_bigger_idx[i] - i)
    return ans


def solve1(n, a):
    return s11(n, a) + s11(n, [-x for x in a])


def main():
    n = ri()
    a = ria()
    wi(solve1(n, a))


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


if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
