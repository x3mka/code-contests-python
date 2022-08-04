import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, ee):
    ans = n * (n-1)

    for i in range(n - 1):
        u, v = ee[i]
        U = min(u, v)
        V = max(u, v)
        x = U * (n - V + 1)
        ans -= x

    return ans


def main():
    n = ri()
    ee = []
    for i in range(n-1):
        ee.append(ria())
    wi(solve(n, ee))


if __name__ == '__main__':
    main()
