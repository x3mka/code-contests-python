import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    diffs = []
    b = [x for x in a]
    for i in range(1, n):
        if a[i] < b[i-1]:
            b[i] = b[i-1]
            diffs.append(b[i-1] - a[i])

    diffs.sort()

    ans = 0
    so_far = 0
    dn = len(diffs)
    for i in range(dn):
        x = diffs[i] - so_far
        ans += x * (dn - i + 1)
        so_far += x

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
