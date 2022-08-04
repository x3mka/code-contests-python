def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, m):
    if n > m:
        t = m
        m = n
        n = t

    # n <= m
    if n == 1:
        return m // 2 + m % 2

    if n % 2 == 0:
        return m * (n // 2)
    if m % 2 == 0:
        return n * (m // 2)

    # both odd
    return solve(n-1, m-1) + solve(n, 1) + solve(1, m-1)


def main():
    for _ in range(ri()):
        n, m = ria()
        print(solve(n, m))


if __name__ == '__main__':
    main()
