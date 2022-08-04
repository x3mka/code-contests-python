import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


# k is odd
def go(n, k):
    if k % 4 == 1:
        return True
    return n % 2 == 0


def solve(n, a):
    for bit in range(32, -1, -1):
        cnt = 0
        for i in range(n):
            if (a[i] & (1 << bit)) > 0:
                cnt += 1
        if cnt % 2 == 0:
            continue

        if go(n, cnt):
            ws('WIN')
        else:
            ws('LOSE')
        return

    ws('DRAW')


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
