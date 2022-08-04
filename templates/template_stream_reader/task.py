# by line input read
import sys
def rs(): return sys.stdin.readline().strip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def prn(n): sys.stdout.write(str(n))
def pia(a): sys.stdout.write(' '.join([str(s) for s in a]))
def by_line_num_reader():
    nums = ria()
    while len(nums) > 0:
        yield from nums
        nums = ria()


# by num input read
import gc, os


ii = 0
_inp = b''


def fast_num_reader():
    def read_char():
        global ii, _inp
        if ii >= len(_inp):
            _inp = os.read(0, 100000)
            gc.collect()
            ii = 0
        if not _inp:
            return b' '[0]
        ii += 1
        return _inp[ii - 1]

    def read_int():
        c = read_char()
        if c == b'-'[0]:
            x = 0
            sign = 1
        else:
            x = c - b'0'[0]
            sign = 0
        c = read_char()
        while c >= b'0'[0]:
            x = 10 * x + c - b'0'[0]
            c = read_char()
        if c == b'\r'[0]:
            read_char()
        return -x if sign else x

    while True:
        yield read_int()


def solve(n, k, reader):
    return 0


def main(reader=by_line_num_reader()):
    t = next(reader)
    for _ in range(t):
        n = next(reader)
        k = next(reader)
        prn(solve(n, k, reader))


if __name__ == '__main__':
    main(reader=fast_num_reader())
