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


def solve(n, m, s, c):
    c_counter = Counter(c)

    ans = 0
    l = 0
    cur_counter = Counter()
    for r in range(n):
        cur_counter[s[r]] = cur_counter.get(s[r], 0) + 1
        while not is_less_or_equal(cur_counter, c_counter):
            cur_counter[s[l]] -= 1
            if cur_counter[s[l]] == 0:
                del cur_counter[s[l]]
            l += 1
        if is_less_or_equal(cur_counter, c_counter):
            ans += r - l + 1
    return ans


def main():
    n, m = ria()
    s = rs()
    c = rs()
    wi(solve(n, m, s, c))


if __name__ == '__main__':
    main()