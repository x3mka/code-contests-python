import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')




def solve(n, a):
    base = 0
    for i in range(0, n, 2):
        base += a[i]

    ans = base

    # even indexes
    l = 0
    best = 0
    s = 0
    for r in range(n // 2):
        s += (a[2*r+1] - a[2*r])
        while s < 0:
            s -= (a[2*l+1] - a[2*l])
            l += 1
        if s > best:
            best = s
            ans = max(ans, base + best)

    # odd indexes
    l = 0
    best = 0
    s = 0
    for r in range((n-1) // 2):
        s += (a[2 * r + 1] - a[2 * r + 2])
        while s < 0:
            s -= (a[2 * l + 1] - a[2 * l + 2])
            l += 1
        if s > best:
            best = s
            ans = max(ans, base + best)

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
