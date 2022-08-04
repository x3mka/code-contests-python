import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    a = [abs(a[i]) * (1 if i % 2 == 0 else -1) for i in range(n)]
    c1 = 0
    c2 = 0
    for i in range(1, n):
        if a[i] - a[i - 1] >= 0:
            c1 += 1
        if a[i] - a[i - 1] <= 0:
            c2 += 1

    assert c1 >= n // 2 and c2 >= n // 2
    return a


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wia(solve(n, a))


if __name__ == '__main__':
    main()
