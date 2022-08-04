import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


class SegmentTree:

    def __init__(self, data, combine_fn=lambda x,y: x+y, default_leaf_fn=lambda x: x, default_node_val=0):
        """Create the segment tree for array data. Complexity: O(n)."""
        self._combine_fn = combine_fn
        self._default_leaf_fn = default_leaf_fn
        self._default_node_val = default_node_val

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [self._default_node_val] * (2 * self._size)
        self.data[self._size:self._size + self._len] = list(map(self._default_leaf_fn, data))
        for idx in range(self._size-1, 0, -1):
            self._fix_node(idx)

    def _parent(self, idx):
        return idx >> 1

    def _left(self, idx):
        return 2 * idx

    def _right(self, idx):
        return 2 * idx + 1

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        self._fix_up_to_root(self._parent(idx))

    def __len__(self):
        return self._len

    # Computes the value of an internal node from the children
    def _fix_node(self, idx):
        self.data[idx] = self.data[self._left(idx)] + self.data[self._right(idx)]

    # Computes the value of each internal node, from the given one up to the root.
    def _fix_up_to_root(self, idx):
        while idx >= 1:
            self._fix_node(idx)
            idx = self._parent(idx)

    def get_data(self):
        """Returns a list of the values stored in the array"""
        return self.data[self._size:self._size + self._len]

    def update(self, idx, x):
        """Update the element at index i to += x. Complexity: O(log n)"""
        idx += self._size
        self.data[idx] += x
        self._fix_up_to_root(self._parent(idx))

    def _query(self, left, right, idx, lx, rx):
        """Query subroutine: given node idx covering segment [lx, rx], query for segment [left, right]"""
        if right < lx or left > rx:
            return self._default_node_val  # node's interval completely out of query interval
        elif left <= lx and rx <= right:
            return self.data[idx]  # node's interval completely contained in query interval
        else:
            mid = (lx + rx) // 2
            res_left = self._query(left, right, self._left(idx), lx, mid)
            res_right = self._query(left, right, self._right(idx), mid+1, rx)
            return self._combine_fn(res_left, res_right)

    def query(self, left, right):
        """Returns the sum of all the elements from index left to index right (inclusive). Complexity: O(log n)"""
        return self._query(left, right, 1, 0, self._size-1)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


def main():
    n, m = ria()
    a = ria()
    st = SegmentTree(a)

    for _ in range(m):
        op, x, y = ria()
        if op == 1:
            st[x] = y
        if op == 2:
            print(st.query(x, y-1))


if __name__ == '__main__':
    main()
