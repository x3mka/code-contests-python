import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                ans = max(ans, a[i] | a[j] | a[k])
    return ans


def main():
    n = ri()
    a = ria()
    wi(solve(n, a))


if __name__ == '__main__':

    main()
