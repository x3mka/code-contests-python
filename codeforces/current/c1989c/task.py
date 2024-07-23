import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a, b):
    ones = sum([1 for i in range(n) if a[i] == b[i] == 1])
    minus_ones = sum([1 for i in range(n) if a[i] == b[i] == -1])

    ones_and_less = sum([1 for i in range(n) if a[i] == 1 and b[i] <= 0])
    less_and_ones = sum([1 for i in range(n) if a[i] <= 0 and b[i] == 1])

    r1 = ones_and_less
    r2 = less_and_ones

    while ones > 0:
        if r1 < r2:
            r1 += 1
        else:
            r2 += 1
        ones -= 1

    while minus_ones > 0:
        if r1 > r2:
            r1 -= 1
        else:
            r2 -= 1
        minus_ones -= 1

    return min(r1, r2)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        wi(solve(n, a, b))


if __name__ == '__main__':
    main()
