import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def f(a):
    return 0


def solve(n, s):
    if n <= 2:
        return int(s)

    sa = list(map(int, list(s)))

    ans = sys.maxsize
    for k in range(n-1):  # we combine a[k] and a[k+1]
        ch = sa[k+1] if sa[k] == 0 else sa[k] * 10 + sa[k+1]
        a = sa[:k] + [ch] + sa[k+2:]

        zeros = sum(1 for x in a if x == 0)
        ones = sum(1 for x in a if x == 1)

        cur_ans = sum(a)
        if zeros > 0:
            cur_ans = 0
        else:
            if ones == n-1:
                cur_ans = 1
            else:
                cur_ans = sum(a) - ones

        ans = min(ans, cur_ans)

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        wi(solve(n, s))


if __name__ == '__main__':
    main()
