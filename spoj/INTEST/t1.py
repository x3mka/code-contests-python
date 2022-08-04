def ri(): return int(input())
def ria(): return list(map(int, input().split()))

import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    n, k = ria()
    cnt = 0
    for _ in range(n):
        a = ri()
        if a % k == 0:
            cnt += 1
    print(cnt)


# 1.29 secs, 27M memory
if __name__ == '__main__':
    main()