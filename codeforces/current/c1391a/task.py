import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')




def test(n, a):
    for i in range(n):
        for j in range(i, n):
            cnt = 0
            for k in range(i, j + 1):
                cnt |= a[k]
            if cnt < j - i + 1:
                return False
    return True

from itertools import permutations


def solve(n):
    wia([i + 1 for i in range(n)])
    return

    ws('================')
    wi(n)

    for p in permutations(a):
        b = list(p)
        if test(n, b):
            wia(b)


def main():
    for _ in range(ri()):
        n = ri()
        solve(n)


if __name__ == '__main__':
    main()
