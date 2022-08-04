import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter


def solve(s):
    c = Counter(s)
    mx = max(c.values())
    for k, v in c.items():
        if mx == v:
            if k == 'R':
                ws('P' * len(s))
            if k == 'S':
                ws('R' * len(s))
            if k == 'P':
                ws('S' * len(s))
            return


def main():
    for _ in range(ri()):
        s = rs()
        solve(s)


if __name__ == '__main__':
    main()
