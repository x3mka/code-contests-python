import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


MOD = 1000000007


def mul(x, y, ):
    return (x * y) % MOD


def bin_pow(x, y):
    z = 1
    while y > 0:
        if y % 2 == 1:
            z = mul(z, x)
        x = mul(x, x)
        y //= 2
    return z


def solve(n, p, a):
    if p == 1:
        return n % 2 == 0

    s = 0
    a = sorted(a, reverse=True)
    for i in range(n):
        c = bin_pow(p, a[i])
        if s == 0:
            s = c
        else:
            s = (s + (MOD - c)) % MOD
    return s


def main():
    for _ in range(ri()):
        n, p = ria()
        a = ria()
        wi(solve(n, p, a))


if __name__ == '__main__':
    main()
