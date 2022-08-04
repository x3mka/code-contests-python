import io
import os
import sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
out = io.StringIO()
# out = io.BytesIO()


def main():
    n = int(input())
    for i in range(n):
        a, b = list(map(int, input().split(b' ')))
        c = a * b
        out.write(str(c))
        out.write('\n')
        # out.write(str(c).encode())
        # out.write(b'\n')
    # os.write(1, out.getvalue())
    sys.stdout.write(out.getvalue())


if __name__ == '__main__':
    main()