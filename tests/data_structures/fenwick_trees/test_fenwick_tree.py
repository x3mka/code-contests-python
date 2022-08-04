from nose.tools import *
from lib.data_structures.fenwick_trees.fenvick_tree import FenwickTree


def test_query():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    ft = FenwickTree.from_array(a)
    assert_equal(ft.query(0), 2)
    assert_equal(ft.query(1), 3)
    assert_equal(ft.query(2), 4)
    assert_equal(ft.query(3), 7)
    assert_equal(ft.query(len(a)-1), 51)


def test_query_range():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    ft = FenwickTree.from_array(a)
    assert_equal(ft.query_range(3, 5), 8)


def test_update():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    ft = FenwickTree.from_array(a)
    ft.update(3, 6) # a[3] += 6
    assert_equal(ft.query_range(3, 5), 14)


def test_find_kth_smallest():
    a = [0, 0, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    ft = FenwickTree.from_array(a)
    assert_equal(ft.find_kth_smallest(0), 1)
    assert_equal(ft.find_kth_smallest(6), 4)
