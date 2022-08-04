import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def ok(a, b, x):
    return True


def solve(n, a, b):
    lo = 0
    hi = min(a[0], b[0])
    while hi > lo:
        m = (lo + hi) // 2
        if ok(a, b, m):
            return

    return False



def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        ws('YES' if solve(n, a, b) else 'NO')


if __name__ == '__main__':
    main()
