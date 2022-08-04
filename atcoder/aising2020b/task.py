import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k):
    return 0


def main():
    n = ri()
    a = ria()
    cnt = 0
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == 1:
            cnt += 1
    wi(cnt)


if __name__ == '__main__':
    main()
