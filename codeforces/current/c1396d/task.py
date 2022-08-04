import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, d, m, a):
    big = sorted([ai for ai in a if ai > m], reverse=True)
    small = sorted([ai for ai in a if ai <= m], reverse=True)
    bn = len(big)
    sn = len(small)

    ans = 0
    for x in range(bn + 1):  # how many of big taken
        taken = (x - 1) * (d + 1) + 1
        score = sum(a[:x])
        if taken > n:
            break
        rem = n - taken
        # it's better to precalc sums
        ans = max(ans, sum(big[:x]) + sum(small[:rem]))

    return ans


def main():
    n, d, m = ria()
    a = ria()

    wi(solve(n, d, m, a))


if __name__ == '__main__':
    main()
