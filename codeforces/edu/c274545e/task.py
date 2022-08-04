import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
def flush(): sys.stdout.flush()


def combine(x, y):
    return x[0]+y[0], 0


class SegmentTree:

    def __init__(self, data, combine_fn=combine, default_leaf_fn=lambda x: (x, 0), default_node_val=(0, 0)):
        """Create the segment tree for array data. Complexity: O(n)."""
        self._combine_fn = combine_fn
        self._default_leaf_fn = default_leaf_fn
        self._default_node_val = default_node_val

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [self._default_node_val] * (2 * self._size)
        self.data[self._size:self._size + self._len] = list(map(default_leaf_fn, data))
        for idx in range(self._size-1, 0, -1):
            self.data[idx] = combine_fn(self.data[2 * idx], self.data[2 * idx + 1])

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

    def get(self, idx):
        idx += self._size
        res = self.data[idx][0]
        while idx >= 1:
            res += self.data[idx][1]
            idx >>= 1
        return res

    def _update_range(self, left, right, x, idx, lx, rx):
        if right < lx or left > rx:
            return
        if lx >= left and rx <= right:
            self.data[idx] = (self.data[idx][0], self.data[idx][1] + x)
            return
        mid = (lx + rx) // 2
        self._update_range(left, right, x, 2 * idx, lx, mid)
        self._update_range(left, right, x, 2 * idx + 1, mid + 1, rx)

    def update_range(self, left, right, x):
        return self._update_range(left, right, x, 1, 0, self._size-1)



def main():
    n, m = ria()

    st = SegmentTree([0]*n)

    for _ in range(m):
        xx = ria()
        op = xx[0]
        if op == 1:
            st.update_range(xx[1], xx[2]-1, xx[3])
        if op == 2:
            wi(st.get(xx[1]))


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
