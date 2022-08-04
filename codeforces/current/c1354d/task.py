# by line input read
import sys
def rs(): return sys.stdin.readline().strip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def prn(n): sys.stdout.write(str(n))
def pia(a): sys.stdout.write(' '.join([str(s) for s in a]))
def by_line_num_reader():
    nums = ria()
    while len(nums) > 0:
        yield from nums
        nums = ria()


# by num input read
import gc, os


ii = 0
_inp = b''


def fast_num_reader():
    def read_char():
        global ii, _inp
        if ii >= len(_inp):
            _inp = os.read(0, 100000)
            gc.collect()
            ii = 0
        if not _inp:
            return b' '[0]
        ii += 1
        return _inp[ii - 1]

    def read_int():
        c = read_char()
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
        yield read_int()


class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth_smallest(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1


def solve(n, q, reader):
    a = [0]*n
    tree = FenwickTree(a)
    for i in range(n+q):
        k = next(reader)
        if k > 0:
            tree.update(k-1, 1)
        else:
            x = tree.find_kth_smallest(-k-1)
            tree.update(x, -1)
    i = 0
    while i < n and not a[i]:
        i += 1
    if i == n:
        return 0
    else:
        return i+1


def main(reader=by_line_num_reader()):
    n = next(reader)
    q = next(reader)
    prn(solve(n, q, reader))


if __name__ == '__main__':
    main(reader=fast_num_reader())
