import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    mn = min(a)
    mx = max(a)
    s = set(a)

    for x in range(mn, mx + 1):
        if x not in s:
            return False

    return True


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        ws('YES' if solve(n, a) else 'NO')


if __name__ == '__main__':
    main()
