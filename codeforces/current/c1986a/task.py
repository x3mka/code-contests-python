import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(x1, x2, x3):
    ans = abs(x2-x1) + abs(x3-x1)
    start = min(x1, x2, x3)
    to = max(x1, x2, x3)

    for a in range(start, to+1):
        s = abs(a-x1) + abs(a-x2) + abs(a-x3)
        ans = min(ans, s)

    return ans


def main():
    for _ in range(ri()):
        x1, x2, x3 = ria()
        wi(solve(x1, x2, x3))


if __name__ == '__main__':
    main()
