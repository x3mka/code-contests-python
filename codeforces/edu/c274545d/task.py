import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
def flush(): sys.stdout.flush()


class SegmentTree:

    def __init__(self, data, combine_fn=lambda x,y: x+y, default_leaf_fn=lambda x: x, default_node_val=0):
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

    def __setitem__(self, idx, value):
        """Updates items at idx to value. Complexity: O(log n)"""
        idx += self._size
        self.data[idx] = self._default_leaf_fn(value)
        idx >>= 1
        combine_fn = self._combine_fn
        while idx >= 1:
            self.data[idx] = combine_fn(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def query(self, left, right):
        """Queries range [left, right). Complexity: O(log n)"""
        left += self._size
        right += self._size

        res_left = self._default_node_val
        res_right = self._default_node_val

        combine_fn = self._combine_fn

        while left < right:
            if left & 1:
                res_left = combine_fn(res_left, self.data[left])
                left += 1
            if right & 1:
                right -= 1
                res_right = combine_fn(self.data[right], res_right)
            left >>= 1
            right >>= 1
        return combine_fn(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

    def find_kth(self, k, idx=1):
        """In binary array find idx such that sum[0:idx] = k is 0-based (first one at k=0)"""
        while idx < self._size:
            left_sum = self.data[2 * idx]
            if left_sum >= k:
                idx = 2 * idx
            else:
                idx = 2 * idx + 1
                k -= left_sum
        return idx - self._size


def main():
    n = ri()
    a = ria()

    st = SegmentTree([0]*n*2)

    res = [0]*n

    d = {}
    for i in range(2*n):
        if a[i] not in d:
            d[a[i]] = i
            st[i] = 1
        else:
            res[a[i] - 1] += st.query(d[a[i]] + 1, i)
            st[d[a[i]]] = 0

    a.reverse()

    d = {}
    for i in range(2 * n):
        if a[i] not in d:
            d[a[i]] = i
            st[i] = 1
        else:
            res[a[i] - 1] += st.query(d[a[i]] + 1, i)
            st[d[a[i]]] = 0

    wia(res)


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