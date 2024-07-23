import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def check(a, b):
    an = len(a)
    bn = len(b)
    res = 0

    idx = 0
    for i in range(bn):
        while idx < an and a[idx] != b[i]:
            idx += 1
        if idx == an:
            return res
        idx += 1
        res += 1
    return res


def solve(a, b):
    an = len(a)
    bn = len(b)

    ans = an + bn

    for i in range(0, bn):
        bs = b[i:]
        m = check(a, bs)
        ans = min(ans, an + bn - m)

    return ans


def main():
    for _ in range(ri()):
        a = rs()
        b = rs()
        wi(solve(a, b))


if __name__ == '__main__':
    main()
