import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 6
    if n == 3:
        return 28
    # if n == 4:
    #     return 96

    # 4 corners x 2
    # 8 near corners x 3
    # 4*(n-4) edges x 4
    # 4 x 4
    # 4*(n-4) x 6
    # (n-4)*(n-4) x 8
    return n * n * (n * n - 1) // 2 - (4 * 2 + 8 * 3 + 4 * (n-4) * 4 + 4 * 4 + 4 * (n-4) * 6 + (n-4) * (n-4) * 8) // 2


def main():
    n = ri()
    for i in range(1, n+1):
        wi(solve(i))


if __name__ == '__main__':
    main()
