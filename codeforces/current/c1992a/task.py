import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(a, b, c):
    ar = [a, b, c]
    for _ in range(5):
        ar = sorted(ar)
        ar[0] += 1
    return ar[0] * ar[1] * ar[2]


def main():
    for _ in range(ri()):
        a, b, c = ria()
        wi(solve(a, b, c))


if __name__ == '__main__':
    main()
