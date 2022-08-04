import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(l, r):
    if 2 * l <= r:
        return [l, 2 * l]
    return [-1, -1]


def main():
    for _ in range(ri()):
        l, r = ria()
        wia(solve(l, r))


if __name__ == '__main__':
    main()
