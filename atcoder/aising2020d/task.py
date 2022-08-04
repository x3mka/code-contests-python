import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    x = rs()

    k = int(x, 2)
    d = x.count('1')

    if d > 1:
        k0 = k % (d-1)
    k1 = k % (d+1)

    f = [0] * (n + 1)
    for i in range(1, n+1):
        f[i] = f[i % bin(i).count('1')] + 1

    for i in range(n):
        cnt = 0
        if x[i] == '1' and d - 1 > 0:
            cnt += f[(k0 - pow(2, n - i - 1, d - 1)) % (d - 1)] + 1
        elif x[i] == '0':
            cnt += f[(k1 + pow(2, n - i - 1, d + 1)) % (d + 1)] + 1
        wi(cnt)


if __name__ == '__main__':
    main()
