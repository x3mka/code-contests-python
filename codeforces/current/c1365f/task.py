import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from collections import Counter


def solve(n, a, b):
    if n % 2 == 1 and a[n//2] != b[n//2]:
        return False

    pa = [(min(a[i], a[n - i - 1]), max(a[i], a[n - i - 1])) for i in range(n // 2)]
    pb = [(min(b[i], b[n - i - 1]), max(b[i], b[n - i - 1])) for i in range(n // 2)]

    ca = Counter(pa)
    cb = Counter(pb)
    return ca == cb


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        ws('Yes' if solve(n, a, b) else 'No')


if __name__ == '__main__':

    main()
