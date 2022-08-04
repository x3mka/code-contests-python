import threading
import os
from collections import deque

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
            # self.data[idx] = combine_fn(self.data[self._left(idx)], self.data[self._right(idx)])
            self.data[idx] = combine_fn(self.data[2 * idx], self.data[2 * idx + 1])

    # def _parent(self, idx):
    #     return idx >> 1
    #
    # def _left(self, idx):
    #     return 2 * idx
    #
    # def _right(self, idx):
    #     return 2 * idx + 1

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = self._default_leaf_fn(value)
        # self._fix_up_to_root(self._parent(idx))
        self._fix_up_to_root(idx >> 1)

    def __len__(self):
        return self._len

    def _fix_up_to_root(self, idx):
        """Computes the value of each internal node, from the given one up to the root."""
        combine_fn = self._combine_fn
        while idx >= 1:
            # self.data[idx] = combine_fn(self.data[self._left(idx)], self.data[self._right(idx)])
            self.data[idx] = combine_fn(self.data[2 * idx], self.data[2 * idx + 1])
            # idx = self._parent(idx)
            idx = idx >> 1

    def get_data(self):
        """Returns a list of the values stored in the array"""
        return self.data[self._size:self._size + self._len]

    def update(self, idx, x):
        """Update the element at index i to += x. Complexity: O(log n)"""
        idx += self._size
        self.data[idx] += x
        # self._fix_up_to_root(self._parent(idx))
        self._fix_up_to_root(idx >> 1)

    def _query(self, left, right, idx, lx, rx):
        """Query subroutine: given node idx covering segment [lx, rx], query for segment [left, right]"""
        if right < lx or left > rx:
            return self._default_node_val  # node's interval completely out of query interval
        elif left <= lx and rx <= right:
            return self.data[idx]  # node's interval completely contained in query interval
        else:
            mid = (lx + rx) // 2
            # res_left = self._query(left, right, self._left(idx), lx, mid)
            res_left = self._query(left, right, 2 * idx, lx, mid)
            # res_right = self._query(left, right, self._right(idx), mid+1, rx)
            res_right = self._query(left, right, 2 * idx + 1, mid + 1, rx)
            return self._combine_fn(res_left, res_right)

    def query(self, left, right):
        """Returns the sum of all the elements from index left to index right (inclusive). Complexity: O(log n)"""
        return self._query(left, right, 1, 0, self._size-1)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)



# x and y - (sum, pref, suf, max_sum)
def combine(x, y):
    s = x[0] + y[0]
    pref = max(x[1], x[0]+y[1])
    suf = max(y[2], y[0]+x[2])
    max_sum = max(x[3], y[3], x[2]+y[1])
    return s, pref, suf, max_sum


class MaxSumSegmentTree(SegmentTree):

    def __init__(self, data):
        SegmentTree.__init__(self, data,
                             combine_fn=combine,
                             default_leaf_fn=lambda x: (x, max(x, 0), max(x, 0), max(x, 0)),
                             default_node_val=(0, 0, 0, 0)
                             )

ii = 0
_inp = b''

def fast_num_reader():
    def read_char():
        global ii, _inp
        if ii >= len(_inp):
            _inp = os.read(0, 100000)
            # gc.collect()
            ii = 0
        if not _inp:
            return b''
        ii += 1
        return _inp[ii - 1]

    def read_int():
        c = read_char()
        if c == b'':
            return None
        if c == b'-'[0]:
            x = 0
            sign = 1
        else:
            x = c - b'0'[0]
            sign = 0
        c = read_char()
        while c >= b'0'[0]:
            x = 10 * x + c - b'0'[0]
            c = read_char()
        if c == b'\r'[0]:
            read_char()
        return -x if sign else x

    while True:
        n = read_int()
        yield n
        if n is None:
            break


import io
q = deque()
out = io.StringIO()

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        reader = fast_num_reader()
        for item in iter(reader):
            # print(item)
            q.append(item)


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def queue_reader(self):
        while True:
            if len(q) > 0:
                n = q.popleft()
                if n is None:
                    break
                yield n
            else:
                out.write('x')

    def run(self):
        reader = self.queue_reader()

        n = next(reader)
        m = next(reader)

        a = [0] * n
        st = MaxSumSegmentTree(a)

        for i in range(n):
            st[i] = next(reader)

        out.write(str(st.query(0, n - 1)[3])+"\n")

        for _ in range(m):
            i = next(reader)
            v = next(reader)
            st[i] = v
            out.write(str(st.query(0, n - 1)[3])+"\n")


if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    c.start()


    p.join()
    c.join()

    print(out.getvalue())