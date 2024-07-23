import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


M = 10**9 + 7


def solve(l, r, k):
    return (pow(9 // k + 1, r, M) - pow(9 // k + 1, l, M)) % M


def main():
    for _ in range(ri()):
        l, r, k = ria()
        wi(solve(l, r, k))


if __name__ == '__main__':
    main()
