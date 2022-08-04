import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


MOD = 10**9 + 7


def solve(n, k, a):
    a = sorted(a, reverse=True, key=lambda x: (abs(x), 1 if x >= 0 else -1))
    sign = 1
    for i in range(k):
        if a[i] < 0:
            sign = -sign
        if a[i] == 0:
            sign = 0

    if sign == 0:
        return 0

    if sign == 1:
        ans = 1
        for i in range(k):
            ans = (ans * abs(a[i])) % MOD
        return ans

    if sign == -1:
        cc = []

        more_neg = -1
        for i in range(k, n):
            if a[i] < 0:
                more_neg = i
                break

        more_pos = -1
        for i in range(k, n):
            if a[i] > 0:
                more_pos = i
                break

        taken_neg = -1
        for i in range(k-1, -1, -1):
            if a[i] < 0:
                taken_neg = i
                break

        taken_pos = -1
        for i in range(k - 1, -1, -1):
            if a[i] > 0:
                taken_pos = i
                break

        if more_neg >= 0 and taken_pos >= 0:
            cc.append((taken_pos, more_neg))
        if more_pos >= 0 and taken_neg >= 0:
            cc.append((taken_neg, more_pos))
        if len(cc) == 2 and cc[0][1] * cc[1][0] < cc[1][1] * cc[0][0]:
            cc[0], cc[1] = cc[1], cc[0]

        # cc = sorted(cc, key=lambda x: abs(a[x[1]] / a[x[0]]), reverse=True)

        if len(cc) > 0:
            ans = 1
            for i in range(k):
                if i != cc[0][0]:
                    ans = (ans * a[i]) % MOD
            ans = (ans * a[cc[0][1]]) % MOD
            return ans
        else:
            # product is negative, taking smallest
            ans = 1
            for i in range(k):
                ans = (ans * a[n-i-1]) % MOD
            return ans


import random


def gen():
    for n in range(2, 100):
        for k in range(2, n):
            for t in range(100):
                a = [random.randrange(100) - 100 for _ in range(n)]
                solve(n, k, a)
        wi(n)


def main():
    # gen()
    # return
    n, k = ria()
    a = ria()
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()
