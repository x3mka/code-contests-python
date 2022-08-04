import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter


def solve(n, s):
    c = Counter(s)
    if len(c) == 1:
        return (n + 2) // 3

    if s[0] == s[-1]:
        cnt = 0
        while s[cnt] == s[-1]:
            s.append(s[cnt])
            cnt += 1
        s = s[cnt:]

    ans = 0

    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        ans += (j - i) // 3
        i = j

    return ans


def solve1(n, s):
    ans = 0

    # dp = [[[0]*2 for _ in range(2)] for i in range(n)]

    for i in range(1, n):
        cnt = 0
        nx = (i + 1) % n
        if s[i-1] == 1:
            cnt += 1
        if s[nx] == -1:
            cnt += 1
        if cnt == 1 and not (s[i-1] == 1 and s[i] == -1) and not (s[nx] == -1 and s[i] == 1):
            ans += 1
            s[i] = -s[i]

    return ans


def ok(n, s):
    for i in range(n):
        if s[i] == s[i-1] and s[i] == s[(i + 1) % n]:
            return False
    return True


def solve_naive(n, s):
    s = [si for si in s]
    res = n
    for mask in range(2**n):
        ss = s.copy()
        cnt = 0
        for bit in range(n):
            if (mask & (1 << bit)) > 0:
                cnt += 1
                ss[bit] = -ss[bit]
        if ok(n, ss):
            res = min(res, cnt)
    return res


def gen():
    for n in range(3, 8):
        wi(n)
        for lls in range(n + 1):
            s = 'L' * lls + 'R' * (n - lls)
            s = [si for si in s]
            res1 = solve(n, s)
            res2 = solve_naive(n, s)
            if res1 != res2:
                wia(s)
                wia([res1, res2])
                solve_naive(n, s)
                return


def main():
    # gen()
    # return

    for _ in range(ri()):
        n = ri()
        s = rs()
        # s = [1 if si == 'R' else -1 for si in s]
        s = [si for si in s]
        wi(solve(n, s))


if __name__ == '__main__':
    main()
