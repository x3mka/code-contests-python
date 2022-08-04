import sys
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
# def ri(): return int(input())
# def ria(): return list(map(int, input().split()))


def main():
    n, k = ria()
    cnt = 0
    for _ in range(n):
        a = int(sys.stdin.readline())
        if a % k == 0:
            cnt += 1
    print(cnt)


# 1.67 secs and 9.2M memory - with sys.stdin.readline() wrapped with functions
# 1.51 secs and 9.1M memory - with sys.stdin.readline() inline
# tle - with input()
if __name__ == '__main__':
    main()