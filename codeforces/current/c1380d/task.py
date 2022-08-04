import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, x, k, y, a, b):
    a = [0] + a + [0]
    b = [0] + b + [0]
    n += 2
    m += 2
    pairs = []
    idx = -1
    for i in range(m):
        try:
            idx = a.index(b[i], idx + 1)
        except ValueError:
            return -1
        pairs.append(idx)

    mx = float("inf")

    def kill(middle, l_val, r_val):
        mn = len(middle)
        if mn == 0:
            return 0
        best = mx
        middle.sort()
        for bs_count in range(mn + 1):
            if (mn - bs_count) % k > 0:
                continue
            if bs_count == mn:
                if max(l_val, r_val) > middle[-1]:
                    best = min(best, bs_count * y)
                continue
            best = min(best, bs_count * y + x * (mn - bs_count) // k)
        # return best
        return -1 if best == mx else best

    cnt = 0
    for i in range(len(pairs) - 1):
        res = kill(a[pairs[i] + 1: pairs[i+1]], a[pairs[i]], a[pairs[i+1]])
        if res == -1:
            return -1
        cnt += res

    return cnt


def main():
    n, m = ria()
    x, k, y = ria()
    a = ria()
    b = ria()
    wi(solve(n, m, x, k, y, a, b))


if __name__ == '__main__':
    main()
