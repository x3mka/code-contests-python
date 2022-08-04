from nose.tools import *


def test_build():
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
    st = build(arr)
    assert_equal(get_sum(st, n, 1, 3), 15)


def test_update():
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
    st = build(arr)

    update_value(arr, st, n, 1, 10)

    assert_equal(get_sum(st, n, 1, 3), 22)


