from lib.data_structures.bit_tree import *


def test_get_sum():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = build(a)
    assert get_sum(tree, 5) == 12  # [0,5] range


def test_get_sum_in_range():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = build(a)
    assert get_sum_in_range(tree, 3, 5) == 8


def test_update():
    a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = build(a)

    # a[3] += 6
    update(tree, 3, 6)

    assert get_sum(tree, 5) == 18
