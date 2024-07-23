import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    ans = 0
    x_max = 0
    for x in range(2, n+1):
        k = n // x
        s = x * k * (k + 1) // 2
        if s > ans:
            ans = s
            x_max = x
    return x_max


def main():
    for _ in range(ri()):
        n = ri()
        wi(solve(n))


if __name__ == '__main__':
    main()
