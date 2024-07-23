import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, a):
    ans = sys.maxsize
    #  c[j] is the maximum index of the beginning subsequence whose sum is equal to j.
    c = [-1 for i in range(s+1)]
    k = 0

    for i in range(n):
        for j in range(s, a[i], -1):
            c[j] = max(c[j], c[j - a[i]])
        c[a[i]] = i

        if c[s] >= k:
            ans = min(ans, i - c[s] + 1)
            k = c[s] + 1

    return -1 if ans == sys.maxsize else ans


def main():
    n, s = ria()
    a = ria()
    wi(solve(n, s, a))


if __name__ == '__main__':
    main()