import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from functools import lru_cache


MOD = 10**9 + 7


def to_digits(s):
    return [int(si) for si in s]


# def solve_in_range(sa, sb, m, dig):
#     a = to_digits(sa)
#     b = to_digits(sb)
#     n = len(a)
#
#     # lru cache is 3 times faster and eats less memory than memo with dp array
#     @lru_cache(maxsize=None)
#     def solve(start, low, high, rem):
#         if start == n:
#             return 1 if rem == 0 else 0
#         # if dp[start][rem][low][high] >= 0:
#         #     return dp[start][rem][low][high]
#
#         ans = 0
#
#         lo = a[start]
#         hi = b[start]
#         down = lo if low else 0
#         up = hi if high else 9
#
#         if start % 2 == 1:
#             # only dig can be placed
#             new_rem = (rem * 10 + dig) % m
#             if down <= dig <= up:
#                 ans = (ans + solve(start + 1, low and (lo == dig), high and (hi == dig), new_rem) % MOD) % MOD
#         else:
#             # any except dig can be placed
#             for d in range(down, up + 1):
#                 if d == dig:
#                     continue
#                 new_rem = (rem * 10 + d) % m
#                 ans = (ans + solve(start + 1, low and (lo == d), high and (hi == d), new_rem) % MOD) % MOD
#
#         # dp[start][rem][low][high] = ans
#         return ans
#
#     # dp = [[[[-1] * 2 for ___ in range(2)] for __ in range(m)] for _ in range(n)]
#     return solve(0, True, True, 0)


def solve_up_to(xs, m, dig):
    a = to_digits(xs)
    n = len(a)

    dp = [[[0] * 2 for __ in range(m)] for _ in range(n+1)]
    dp[0][0][1] = 1
    for i in range(n):
        for j in range(m):
            for k in range(2):
                limit = a[i] if k else 9
                for d in range(limit+1):
                    if i % 2 == 1 and d != dig:
                        continue
                    if i % 2 == 0 and d == dig:
                        continue
                    if i == 0 and d == 0:
                        continue
                    ni = i + 1
                    nj = (10 * j + d) % m
                    nk = k and d == a[i]
                    dp[ni][nj][nk] = (dp[ni][nj][nk] + dp[i][j][k]) % MOD

    ans = 0
    for i in range(1, n+1):
        for k in range(2):
            ans = (ans + dp[i][0][k]) % MOD
    return ans


def solve_in_range(a, b, m, dig):
    r1 = solve_up_to(b, m, dig)
    r2 = solve_up_to(str(int(a)-1), m, dig)
    return (r1 - r2) % MOD


def main():
    m, dig = ria()
    a = rs()
    b = rs()
    wi(solve_in_range(a, b, m, dig))


if __name__ == '__main__':
    main()
