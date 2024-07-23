import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(x1, y1, x2, y2):
    if x1 < y1 and x2 < y2 or x1 > y1 and x2 > y2:
        return "YES"
    else:
        return "NO"


def main():
    for _ in range(ri()):
        x1, y1 = ria()
        x2, y2 = ria()
        ws(solve(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
