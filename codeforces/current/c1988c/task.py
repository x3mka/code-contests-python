import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    a = []
    for i in range(62, -1, -1):
        x = 1 << i
        if ((x & n) == x) and (x != n):
            a.append(n - x)
    a.append(n)
    wi(len(a))
    wia(a)


def main():
    for _ in range(ri()):
        n = ri()
        solve(n)


if __name__ == '__main__':
    main()
