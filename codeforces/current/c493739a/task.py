import math
import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


inf = sys.maxsize


def prev_lower_idx(a):
    n = len(a)
    ans = [-1] * n
    stack = []  # increasing monotonic
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans



def solve(n, a):
    dp = [0] * n
    pref = [0] * n
    stack = [0]
    dp_values_sum_on_stack = 1
    dp[0] = 1
    pref[0] = 1

    for i in range(1, n):
        while stack and a[stack[-1]] >= a[i]:
            dp_values_sum_on_stack -= dp[stack[-1]]
            stack.pop()
        if stack:
            dp[i] = dp_values_sum_on_stack + pref[i-1] - pref[stack[-1]]
        else:
            dp[i] = 1 + pref[i-1]

        pref[i] = pref[i-1] + dp[i]
        stack.append(i)
        dp_values_sum_on_stack += dp[i]

    ans = 0
    suffix_min = inf
    for i in range(n - 1, -1, -1):
        suffix_min = min(suffix_min, a[i])
        if a[i] == suffix_min:
            ans += dp[i]
    return ans % 998244353

def solve1(n, a):
    dp = [0] * n
    for i in range(n):
        suffix_min = inf
        # case 1: a[j] in the last second
        # we add to dp[i] only if [j+1 ... i-1] is absorbed by a[j] or a[i] (there is min or less among these two)
        for j in range(i-1, -1, -1):
            suffix_min = min(suffix_min, a[j])
            if a[i] <= suffix_min or a[j] <= suffix_min:
                dp[i] += dp[j]

        # case 2: if a[i] is the smallest, then it can absorb all
        suffix_min = min(suffix_min, a[i])
        if suffix_min == a[i]:
            dp[i] += 1

    ans = 0
    suffix_min = inf
    for i in range(n-1, -1, -1):
        suffix_min = min(suffix_min, a[i])
        if a[i] == suffix_min:
            ans += dp[i]

    return ans % 998244353


def main():
    n = ri()
    a = ria()
    wi(solve(n, a))


if __name__ == '__main__':
    main()
