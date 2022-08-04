import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s):
    c0 = sum(1 for si in s if si == 'AC')
    c1 = sum(1 for si in s if si == 'WA')
    c2 = sum(1 for si in s if si == 'TLE')
    c3 = sum(1 for si in s if si == 'RE')
    ws("AC x {0}".format(c0))
    ws("WA x {0}".format(c1))
    ws("TLE x {0}".format(c2))
    ws("RE x {0}".format(c3))


def main():
    n = ri()
    s = []
    for i in range(n):
        s.append(rs())
    solve(n, s)


if __name__ == '__main__':
    main()
