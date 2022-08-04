import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a, b):
    sa = set(a)
    sb = set(b)

    s = sa.intersection(sb)

    if len(s) == 0:
        ws('NO')
    else:
        ws('YES')
        wia([1, next(iter(s))])


def main():
    for _ in range(ri()):
        n, m = ria()
        a = ria()
        b = ria()
        solve(n, m, a, b)


if __name__ == '__main__':
    main()
