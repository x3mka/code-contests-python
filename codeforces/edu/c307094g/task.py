import sys
from collections import Counter


def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def is_less_or_equal(c1, c2):
    return all([c1[k] <= c2.get(k, 0) for k in c1])


def solve(n, c, s):
    ans = 0
    l = 0
    cur_a = 0
    cur_b = 0
    cur_rude = 0
    for r in range(n):
        if s[r] == 'a':
            cur_a += 1
        if s[r] == 'b':
            cur_b += 1
            cur_rude += cur_a
        while cur_rude > c:
            if s[l] == 'a':
                cur_a -= 1
                cur_rude -= cur_b
            if s[l] == 'b':
                cur_b -= 1
            l += 1
        if cur_rude <= c:
            ans = max(ans, r - l + 1)
    return ans


def main():
    n, c = ria()
    s = rs()
    wi(solve(n, c, s))


if __name__ == '__main__':
    main()