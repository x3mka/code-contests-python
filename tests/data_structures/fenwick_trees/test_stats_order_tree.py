from nose.tools import *
from lib.data_structures.fenwick_trees.stats_order_tree import StatOrderTree


def test_find_kth_smallest():
    a = [2, 1, 3, 2, 4, 5]
    sot = StatOrderTree.from_array(a)
    assert_equal(sot.find_kth_smallest(1), 1)
    assert_equal(sot.find_kth_smallest(2), 2)
    assert_equal(sot.find_kth_smallest(3), 2)
    assert_equal(sot.find_kth_smallest(4), 3)
    assert_equal(sot.find_kth_smallest(5), 4)
    assert_equal(sot.find_kth_smallest(6), 5)


def test_delete():
    a = [2, 1, 3, 2, 4, 5]
    sot = StatOrderTree.from_array(a)
    assert_equal(sot.find_kth_smallest(1), 1)
    sot.delete(1)
    assert_equal(sot.find_kth_smallest(1), 2)
    sot.delete(2)
    assert_equal(sot.find_kth_smallest(1), 2)
    sot.delete(2)
    assert_equal(sot.find_kth_smallest(1), 3)
    sot.delete(3)
    assert_equal(sot.find_kth_smallest(1), 4)
    sot.delete(4)
    assert_equal(sot.find_kth_smallest(1), 5)
    sot.delete(5)
    assert_equal(sot.find_kth_smallest(1), -1)


