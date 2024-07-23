import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    if n == 0:
        return "NO"
    a.sort(reverse=True)
    mx = a[0]
    c = sum([1 for i in range(n) if a[i] == mx])
    return "YES" if c % 2 == 1 else solve(n-c, a[c:])


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        ws(solve(n, a))


if __name__ == '__main__':
    main()
