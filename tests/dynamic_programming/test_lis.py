from lib.dynamic_programming.lis import lis


def test():
    a = [1, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    s = lis(a)
    assert s == [1, 2, 6, 9, 11, 15]
