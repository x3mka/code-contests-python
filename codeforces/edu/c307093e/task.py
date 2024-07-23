import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k, a):
    ans = 0
    l = 0
    cur = {}
    for r in range(n):
        cur[a[r]] = cur.get(a[r], 0) + 1
        while len(cur) > k:
            cur[a[l]] -= 1
            if cur[a[l]] == 0:
                del cur[a[l]]
            l += 1
        ans += r - l + 1

    return ans


def main():
    n, k = ria()
    a = ria()
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()