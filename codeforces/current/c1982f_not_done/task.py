import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return [int(_) for _ in sys.stdin.readline().split()]
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')
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
        # return self._tree_repr()

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


# min
class MinSegmentTree(SegmentTree):

    def __init__(self, data, default=sys.maxsize):
        # SegmentTree.__init__(self, data, default, lambda x, y: min(x, y))
        SegmentTree.__init__(
            self, data,
            combine_fn=lambda x, y: min(x + y),
            default_leaf_fn=lambda x: x,
            default_node_val=default
        )


# max
class MaxSegmentTree(SegmentTree):

    def __init__(self, data, default=-sys.maxsize-1):
        # SegmentTree.__init__(self, data, default, lambda x, y: max(x, y))
        SegmentTree.__init__(
            self, data,
            combine_fn=lambda x, y: max(x + y),
            default_leaf_fn=lambda x: x,
            default_node_val=default
        )


class MinMaxSegmentTree(SegmentTree):

    def __init__(self, data):
        # SegmentTree.__init__(
        #     self, data,
        #     (sys.maxsize, -sys.maxsize-1),
        #     lambda x, y: (min(x[0],y[0]), max(x[1], y[1]))
        # )
        SegmentTree.__init__(
            self, data,
            combine_fn=lambda x, y: (min(x[0],y[0]), max(x[1], y[1])),
            default_leaf_fn=lambda x: (x, x),
            default_node_val=(sys.maxsize, -sys.maxsize-1)
        )



# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SortedList.py
class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i : i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError("{0!r} not in list".format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return "SortedList({0})".format(list(self))


import heapq


class MinHeap:
    def __init__(self, data):
        self.data = data
        heapq.heapify(self.data)

    def __len__(self):
        return len(self.data)

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)


class MaxHeap:
    def __init__(self, data):
        self.data = [-item for item in data]
        heapq.heapify(self.data)

    def __len__(self):
        return len(self.data)

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)


class SortedSet:
    def __init__(self, data):
        self.min_heap = MinHeap(data)
        self.max_heap = MaxHeap(data)

    def __len__(self):
        return len(self.min_heap)

    def min(self):
        return self.min_heap.top()

    def max(self):
        return self.max_heap.top()

    def push(self, val):
        self.min_heap.push(val)
        self.max_heap.push(val)



def solve(n, a, q, updates):
    res = []
    tree = MinMaxSegmentTree(a)
    # min_tree = MinSegmentTree(a)
    # max_tree = MaxSegmentTree(a)

    # s = SortedList()
    s = SortedSet([i for i in range(1, n) if a[i] < a[i-1]])

    def bs_l(start, end, val):
        while end - start > 1:
            m = (start + end) // 2
            if a[m] > val:
                end = m
            else:
                start = m
        return end

    def bs_r(start, end, val):
        while end - start > 1:
            m = (start + end) // 2
            if a[m] < val:
                start = m
            else:
                end = m
        return start

    def go():
        if len(s) == 0:
            res.append("{0} {1}".format(-1, -1))
            # wia([-1, -1])
            return

        pos_min = s[0]   # prefix till pos_min-1 already sorted
        pos_max = s[-1]   # suffix after pos_max already sorted

        min_val, max_val = tree.query(pos_min-1, pos_max+1)
        # min_val = min_tree.query(pos_min-1, pos_max+1)
        # max_val = max_tree.query(pos_min-1, pos_max+1)

        l = bs_l(-1, pos_min-1, min_val)
        r = bs_r(pos_max, n, max_val)

        res.append("{0} {1}".format(l+1, r+1))
        # wia([l+1, r+1])

    go()

    for i in range(q):
        idx, val = updates[i]
        idx -= 1

        a[idx] = val
        tree[idx] = val
        # min_tree[idx] = val
        # max_tree[idx] = val

        # if idx in s:
        # s.discard(idx)
        # # if idx+1 in s:
        # s.discard(idx+1)
        if idx > 0 and a[idx] < a[idx-1]:
            s.push(idx)
        if idx < n-1 and a[idx+1] < a[idx]:
            s.push(idx+1)

        while len(s) > 0:
            m = s.min()

        go()

    ws("\n".join(res))


class FastReader(io.IOBase):
    newlines = 0

    def __init__(self, fd, chunk_size=1024*64):
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


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        q = ri()
        updates = [[] for _ in range(q)]
        for i in range(q):
            updates[i] = ria()
        solve(n, a, q, updates)


if __name__ == '__main__':
    sys.stdin = FastStdin()
    sys.stdout = FastStdout()
    main()
