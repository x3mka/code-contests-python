import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def pow_mod(n, m, mod=1000000007):
    ans = 1
    while m:
        if m & 1:
            ans = (ans * n) % mod
        m >>= 1
        n = (n * n) % mod
    return ans


def main():
    n = ri()
    mod = 10**9 + 7
    wi(pow_mod(2, n, mod))


if __name__ == '__main__':
    main()
