import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(l, r, m):
    for a in range(l, r+1):
        n = max((m + l - r + a - 1) // a, 1)
        if n <= (m + r - l) // a:
            s = n * a - m   # c - b
            if s >= 0:
                c = r
                b = r - s
            else:
                c = l
                b = l - s
            if l <= b <= r:
                return([a, b, c])


def main():
    for _ in range(ri()):
        l, r, m = ria()
        wia(solve(l, r, m))


if __name__ == '__main__':
    main()
