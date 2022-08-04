from nose.tools import *
from lib.data_structures.sparse_table import SparseTable
import random


def test():
    a = [4, 6, 1, 5, 7, 3]
    st = SparseTable(a)

    assert_equal(st.query(3, 5), 3)
    assert_equal(st.query(0, 5), 1)
    assert_equal(st.query(0, 3), 1)
    assert_equal(st.query(0, 1), 4)
    assert_equal(st.query(4, 4), 7)


def test1():
    n = 100
    mx = 100
    a = [random.randrange(mx) for _ in range(n)]
    st = SparseTable(a)
    for l in range(n):
        for r in range(l, n):
            assert st.query(l, r) == min(a[l:r+1])


