import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def prev_lower_idx(n, a):
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def next_lower_idx(n, a):
    ans = [n] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def solve(n, a):
    left = prev_lower_idx(n, a)
    right = next_lower_idx(n, a)
    left_extension = [0] * n
    right_extension = [0] * n
    cover = [0] * n
    ans = a[0]
    for i in range(n):
        left_extension[i] = i - left[i] - 1
        right_extension[i] = right[i] - i - 1
        cover[i] = a[i] * (left_extension[i] + right_extension[i] + 1)
        ans = max(ans, cover[i])
    wia(left_extension)
    wia(right_extension)
    wia(cover)
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


if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
