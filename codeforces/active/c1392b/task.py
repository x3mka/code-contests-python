import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k, a):
    kk = min(k, 10)
    for d in range(kk):
        mx = max(a)
        a = [mx - ai for ai in a]
    for d in range((k - kk) % 2):
        mx = max(a)
        a = [mx - ai for ai in a]
    return a


def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        wia(solve(n, k, a))
        # ws('===================')


if __name__ == '__main__':
    main()
