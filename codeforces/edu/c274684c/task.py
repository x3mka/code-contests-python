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
        # return "SegmentTree({0})".format(self.data)
        return self._tree_repr()

    def _tree_repr(self):
        def recursive_repr(i):
            if i >= self._size:
                return [str(self.data[i])]

            left = recursive_repr(2 * i)
            right = recursive_repr(2 * i + 1)
            lines = ["{}   {}".format(l, r) for l, r in zip(left, right)]

            width = len(lines[0])
            left_width = len(left[0]) // 2
            right_width = len(right[0]) // 2
            stem_width = width - left_width - right_width - 2

            branches = " " * left_width + "/" + " " * stem_width + "\\" + " " * right_width
            stem = [" "] * (left_width + 1) + ["_"] * stem_width + [" "] * (right_width + 1)
            stem[width // 2] = "^"

            lines.append(branches)
            lines.append("".join(stem))
            lines.append(str(self.data[i]).center(width))
            return lines

        return "\n".join(reversed(recursive_repr(1)))


# (inv_count, counter as OrderedDict
def combine(x, y):
    cnt = 0
    z = []

    i = 0
    j = 0

    a = x[1]
    b = y[1]

    # counting inversions like in merge for merge-sort
    left = 0
    all_left = sum([v[1] for v in a])

    while i < len(a) and j < len(b):

        # no inversions if arr[i] <= arr[j]
        if a[i][0] <= b[j][0]:
            if len(z) > 0 and z[-1][0] == a[i][0]:
                z[-1] = (z[-1][0], z[-1][1] + a[i][1])
            else:
                z.append((a[i][0], a[i][1]))
            left += a[i][1]
            i += 1
        else:
            # there are inversions
            if len(z) > 0 and z[-1][0] == b[j][0]:
                z[-1] = (z[-1][0], z[-1][1] + b[j][1])
            else:
                z.append((b[j][0], b[j][1]))
            cnt += (all_left - left) * b[j][1]
            j += 1

    while i < len(a):
        if len(z) > 0 and z[-1][0] == a[i][0]:
            z[-1] = (z[-1][0], z[-1][1] + a[i][1])
        else:
            z.append((a[i][0], a[i][1]))
        left += a[i][1]
        i += 1

    while j < len(b):
        if len(z) > 0 and z[-1][0] == b[j][0]:
            z[-1] = (z[-1][0], z[-1][1] + b[j][1])
        else:
            z.append((b[j][0], b[j][1]))
        j += 1

    return x[0]+y[0]+cnt, z


def default_leaf_fn(x):
    return 0, [(x, 1)]


def default_node_fn():
    return 0, []


def inv_count(a, left, right):
    cnt = 0
    for i in range(left, right-1):
        for j in range(i+1, right):
            if a[i] > a[j]:
                cnt += 1
    return cnt


def main():
    n, q = ria()
    a = ria()

    st = SegmentTree(a, combine_fn=combine, default_leaf_fn=default_leaf_fn, default_node_val=default_node_fn())

    for _ in range(q):
        xx = ria()
        op = xx[0]
        if op == 1:
            wi(st.query(xx[1]-1, xx[2])[0])  # query
        if op == 2:
            st[xx[1]-1] = xx[2]


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
