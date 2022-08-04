import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(x, y, n):
    d = n // x
    ans = d * x + y
    if ans > n:
        ans -= x
    return ans


def main():
    for _ in range(ri()):
        x, y, n = ria()
        wi(solve(x, y, n))


if __name__ == '__main__':
    main()
