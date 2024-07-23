import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, w, c):
    ans = 0
    l = 0
    cur_w = 0
    cur_c = 0
    for r in range(n):
        cur_w += w[r]
        cur_c += c[r]
        while cur_w > s:
            cur_w -= w[l]
            cur_c -= c[l]
            l += 1
        if cur_w <= s:
            ans = max(ans, cur_c)
    return ans


def main():
    n, s = ria()
    w = ria()
    c = ria()
    wi(solve(n, s, w, c))


if __name__ == '__main__':
    main()