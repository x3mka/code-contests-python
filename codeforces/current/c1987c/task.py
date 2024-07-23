import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, h):
    ans = h[n-1]

    for i in range(n-2, -1, -1):
        ans = max(ans+1, h[i])

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        h = ria()
        wi(solve(n, h))


if __name__ == '__main__':
    main()
