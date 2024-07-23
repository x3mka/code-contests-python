import sys
from itertools import product, accumulate


def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def get_pre(n, a):
    pre = [0] * (n + 1)
    for i in range(1, n+1):
        pre[i] = pre[i - 1] + a[i - 1]
    return pre[1:]

def test(n, a):
    pre = get_pre(n, a)
    suf = get_pre(n, list(reversed(a)))

    pre_max = max(pre)
    suf_max = max(suf)

    x = pre.index(pre_max)
    y = n - suf.index(suf_max)-1

    return [x, y]



def solve(n, x, y):
    # ws("========================")
    # ix = [[-1, 1]] * n
    # for p in product(*ix):
    #     x1, y1 = test(n, p)
    #     if x == x1 and y == y1:
    #         wia(p)

    pref = list(reversed([-1, 1] * (y // 2) + ([-1] if y % 2 == 1 else [])))
    suf = [-1, 1] * ((n - x - 1) // 2) + ([-1] if (n - x - 1) % 2 == 1 else [])

    # ws('----- ans -------')
    return pref + [1] * (x - y + 1) + suf

def main():
    for _ in range(ri()):
        n, x, y = ria()
        wia(solve(n, x-1, y-1))


if __name__ == '__main__':
    main()
