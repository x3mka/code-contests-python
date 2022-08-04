import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    if a[0] + a[1] <= a[n-1]:
        return [1, 2, n]
    return [-1]


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wia(solve(n, a))


if __name__ == '__main__':
    main()
