import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


INF = 10**10


def solve(n, k, a, w):
    a = sorted(a, reverse=True)
    w = sorted(w)

    ans = 0
    left = 0
    while left < k and w[left] == 1:
        ans += 2 * a[left]
        left += 1

    right = n-1
    for i in range(k-1, -1, -1):
        if w[i] <= 1:
            continue
        ans += a[left] + a[right]
        left += 1
        right -= (w[i]-1)

    return ans


def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        w = ria()
        wi(solve(n, k, a, w))


if __name__ == '__main__':
    main()
