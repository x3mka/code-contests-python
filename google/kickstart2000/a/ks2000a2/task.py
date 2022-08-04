import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a])); sys.stdout.write('\n')


from itertools import accumulate


def solve(n, k, p, s):
    # d[i, j] - max beauty when using only i stacks and not more than j plates
    d = [[0 for j in range(p+1)] for i in range(n+1)]

    pre = [[0] + list(accumulate(s[i])) for i in range(n)]

    for i in range(1, n+1):
        for j in range(p+1):
            d[i][j] = 0
            for w in range(min(j, k)+1):
                d[i][j] = max(d[i][j], d[i-1][j-w] + pre[i-1][w])

    return d[n][p]


def main():
    for t in range(ri()):
        n, k, p = ria()
        s = []
        for _ in range(n):
            s.append(ria())
        ws("Case #{}: {}".format(t+1, solve(n, k, p, s)))


if __name__ == '__main__':
    main()
