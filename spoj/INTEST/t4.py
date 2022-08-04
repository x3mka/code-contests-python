def ri(): return int(input())
def ria(): return list(map(int, input().split()))

import os
from io import IOBase, BytesIO


class TokenReader(IOBase):

    def __init__(self, fd=0, chunk_size=1024*8):
        self.fd = fd
        self.chunk_size = chunk_size
        self.idx = 0
        self.data = b''

    def read_char(self):
        if self.idx >= len(self.data):
            self.data = os.read(self.fd, self.chunk_size)
            # gc.collect()
            self.idx = 0
        if not self.data:
            return b''
        self.idx += 1
        return self.data[self.idx - 1]

    def read_int(self):
        c = self.read_char()
        if c == b'-'[0]:
            x = 0
            neg = 1
        else:
            x = c - b'0'[0]
            neg = 0
        c = self.read_char()
        while c >= b'0'[0]:
            x = 10 * x + c - b'0'[0]
            c = self.read_char()
        if c == b'\n'[0]:
            self.read_char()
        if c == b'\r'[0]:
            self.read_char()
        return -x if neg else x


def main():
    reader = TokenReader()
    n = reader.read_int()
    k = reader.read_int()
    cnt = 0
    for _ in range(n):
        a = reader.read_int()
        if a % k == 0:
            cnt += 1
    print(cnt)


#
if __name__ == '__main__':
    main()