import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, a):
    # wia(a)
    for _ in range(k):
        b = [0] * n
        for i in range(n):
            l = max(0, i - a[i])
            r = min(n-1, i + a[i])
            b[l] += 1
            if r < n-1:
                b[r+1] -= 1
        for i in range(1, n):
            b[i] += b[i-1]
        a = b
        # wia(a)
        if sum(a) == n * n:
            break
    return a


def main():
    n, k = ria()
    a = ria()
    wia(solve(n, k, a))


if __name__ == '__main__':
    main()
