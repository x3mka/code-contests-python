import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from functools import lru_cache


def is_prime(x):
    if x <= 1:
        return False
    if x in [2, 3, 5, 7]:
        return True
    for d in [2, 3, 5, 7]:
        if x % d == 0:
            return False
    return True


def sub_solve(x):
    # ws("========== " + str(x) + " ==============")
    if x <= 0:
        return 0

    @lru_cache(maxsize=None)
    def go(pos, restricted, s):
        """
        :param pos: index value from right in the given integer
        :param restricted: if restricted, digit span is [0,9], otherwise [0,digits[pos]]
        :param s: supporting state
        :return:
        """
        if pos == -1:
            if is_prime(s):
                # wi(''.join(ss) + ' -- ' + str(s))
                return 1
            else:
                return 0

        # check memo value and return it if exists
        # if not restricted and s >= 0 and dp[pos][s + 100] != -1:
        #     return dp[pos][s + 100]

        ans = 0
        up = a[pos] if restricted else 9
        for d in range(up + 1):
            ss.append(str(d))
            ans += go(pos - 1, restricted and d == a[pos], s + d * (-1 if pos % 2 == 0 else 1))
            ss.pop()

        # if not restricted and s >= 0:
        #     dp[pos][s + 100] = ans
        return ans

    a = []
    while x > 0:
        a.append(x % 10)
        x //= 10

    ss = []
    n = len(a)
    dp = [[-1]*200 for _ in range(n)]
    res = go(n-1, True, 0)
    # ws("--- " + str(res) + " ---")
    return res


def solve(a, b):
    return sub_solve(b) - sub_solve(a-1)


def main():
    for _ in range(ri()):
        a, b = ria()
        wi(solve(a, b))



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
