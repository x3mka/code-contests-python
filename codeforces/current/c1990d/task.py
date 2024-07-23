import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def covers(n, p):
    if n == 0:
        return True
    if n > 4:
        return False
    line = [1] * n + [0] * (4 - n)
    return sum([1 for i in range(4) if p[i] >= line[i]]) == 4


def solve(n, a):
    ans = 0
    b1 = 0  # [1,2] set
    b2 = 0  # [3,4] set

    for i in range(n):
        if b1 == 0 and b2 == 0:
            if a[i] == 0:
                continue
            ans += 1
            if a[i] <= 2:
                b1 = 1
        elif b1 == 1:
            b1 = 0
            if a[i] <= 2:
                continue
            ans += 1
            if a[i] <= 4:
                b2 = 1
        else:
            b2 = 0
            if a[i] == 0:
                continue
            ans += 1
            if a[i] <= 4:
                b1 = 1

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
