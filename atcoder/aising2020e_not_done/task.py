import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')



# def can(x, n, a):



def solve(n, a):
    lo = 0
    hi = sum(ai[1] + ai[2] for ai in a)
    while hi > lo + 1:
        x = (lo + hi) // 2
        if can(x, n, a):
            lo = x
        else:
            hi = x
    return lo


def main():
    for _ in range(ri()):
        n = ri()
        a = []
        for i in range(n):
            a.append(ria())
        wi(solve(n, a))


if __name__ == '__main__':
    main()
