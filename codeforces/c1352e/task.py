def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


#from bitarray import bitarray


import array
def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5                   # number of 32 bit integers
    if (bitSize & 31):                      # if bitSize != (32 * n) add
        intSize += 1                        #    a record for stragglers
    if fill == 1:
        fill = 4294967295                                 # all bits set
    else:
        fill = 0                                      # all bits cleared

    bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

    bitArray.extend((fill,) * intSize)

    return(bitArray)

# testBit() returns a nonzero result, 2**offset, if the bit at 'bit_num' is set to 1.
def testBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return(array_name[record] & mask)

# setBit() returns an integer with the bit at 'bit_num' set to 1.
def setBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] |= mask
    return(array_name[record])


def solve(n, a):
    s = [a[0]]
    for i in range(1, n):
        s.append(s[i-1] + a[i])
    m = max(a)

    d = makeBitArray(s[n-1]+1)
    #d.setall(False)

    for i in range(n-1):
        for j in range(i+1, n):
            ss = s[j] - s[i] + a[i]
            if ss > m:
                continue
            if not testBit(d, ss):
                setBit(d, ss)
    return len([x for x in a if testBit(d, x)])


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        print(solve(n, a))


if __name__ == '__main__':
    main()
