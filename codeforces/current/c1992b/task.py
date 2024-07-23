import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k, a):
    a = sorted(a)
    mx = a[-1]
    to_one = 0
    for i in range(k-1):
        to_one += a[i]-1
    return n - mx + to_one


def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        wi(solve(n, k, a))


if __name__ == '__main__':
    main()
