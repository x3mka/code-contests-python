import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, s, A, B, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)

    pre_a = [0] * (n+1)
    pre_b = [0] * (m+1)
    for i in range(1, n+1):
        pre_a[i] = pre_a[i-1] + a[i-1]
    for i in range(1, m+1):
        pre_b[i] = pre_b[i-1] + b[i-1]

    ans = 0
    for i in range(n+1):
        if i * A > s:
            break
        j = min((s - i * A) // B, m)
        ans = max(ans, pre_a[i] + pre_b[j])

    return ans


def main():
    n, m, s, A, B = ria()
    a = ria()
    b = ria()
    wi(solve(n, m, s, A, B, a, b))


if __name__ == '__main__':
    main()