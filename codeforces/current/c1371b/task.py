import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, r):
    m = min(n-1, r)
    return m * (m + 1) // 2 + (1 if r >= n else 0)


def main():
    for _ in range(ri()):
        n, r = ria()
        wi(solve(n, r))


if __name__ == '__main__':
    main()
