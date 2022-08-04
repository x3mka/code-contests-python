def ri(): return int(input())
def ria(): return list(map(int, input().split()))

import io
import sys
input = io.StringIO(sys.stdin.read()).readline


def main():
    n, k = ria()
    cnt = 0
    for _ in range(n):
        a = ri()
        if a % k == 0:
            cnt += 1
    print(cnt)


# 1.46 secs, 100M memory
if __name__ == '__main__':
    main()