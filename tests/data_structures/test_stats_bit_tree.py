from nose.tools import *
from lib.data_structures.stats_bit_tree import *


def test_build():
    a = [3, 1, 2, 1, 3, 4]
    max_n = max(a)+1
    tree = build_stats_tree(max_n)
    for i in range(len(a)):
        insert(tree, a[i])

    assert_equal(tree, [0, 0, 2, 1, 5, 1, 1])
    assert_equal(get_sum(tree, 5), 6)  # number of elements


def test_kth_smallest():
    a = [3, 1, 2, 1, 3, 4]
    max_n = max(a)+1
    tree = build_stats_tree(max_n)
    for i in range(len(a)):
        insert(tree, a[i])

    assert find_kth_smallest(tree, 1) == 1
    assert find_kth_smallest(tree, 2) == 1
    assert find_kth_smallest(tree, 3) == 2
    assert find_kth_smallest(tree, 4) == 3
    assert find_kth_smallest(tree, 5) == 3
    assert find_kth_smallest(tree, 6) == 4


