from nose.tools import *
from lib.data_structures.fenwick_trees.fenvick_tree_min import FenwickTreeMin


def test_query():
    a = [3, 2, 1, 1, 3, 2]
    ft = FenwickTreeMin.from_array(a)
    assert_equal(ft.query(0), 3)
    assert_equal(ft.query(1), 2)
    assert_equal(ft.query(2), 1)
    assert_equal(ft.query(4), 1)
    assert_equal(ft.query(5), 1)


def test_update():
    a = [3, 2, 1, 1, 3, 2]
    ft = FenwickTreeMin.from_array(a)
    ft.update(2, 0)
    ft.update(3, 0)
    assert_equal(ft.query(5), 0)


