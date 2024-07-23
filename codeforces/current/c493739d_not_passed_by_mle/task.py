import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


inf = sys.maxsize


def solve(n, a):
    dp = [0] * n
    pref = [0] * n
    stack = [0]
    dp_values_sum_on_stack = 1
    dp[0] = 1
    pref[0] = 1

    for i in range(1, n):
        while stack and a[stack[-1]] >= a[i]:
            dp_values_sum_on_stack -= dp[stack[-1]]
            stack.pop()
        if stack:
            dp[i] = dp_values_sum_on_stack + pref[i-1] - pref[stack[-1]]
        else:
            dp[i] = 1 + pref[i-1]

        pref[i] = pref[i-1] + dp[i]
        stack.append(i)
        dp_values_sum_on_stack += dp[i]

    ans = 0
    suffix_min = inf
    for i in range(n - 1, -1, -1):
        suffix_min = min(suffix_min, a[i])
        if a[i] == suffix_min:
            ans += dp[i]
    return ans % 998244353




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
