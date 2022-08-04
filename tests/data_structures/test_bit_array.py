from lib.data_structures.bit_array import BitArray


def test():
    n = 10000
    array = BitArray(n)

    for i in range(n):
        assert array[i] == 0
        array[i] = 1
        assert array[i] == 1

    for i in range(n):
        assert array[i] == 1
        array[i] = 0
        assert array[i] == 0




