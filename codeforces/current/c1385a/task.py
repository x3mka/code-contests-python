import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(ar):
    ar.sort()
    b = ar[0]
    c = ar[1]
    if max(b, c) == ar[2]:
        ws('YES')
        wia([1, ar[0], ar[1]])
        return
    ws('NO')


def main():
    for _ in range(ri()):
        ar = ria()
        solve(ar)


if __name__ == '__main__':
    main()
