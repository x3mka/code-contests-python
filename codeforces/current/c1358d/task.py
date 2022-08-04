def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def nn2(n):
    return n * (n+1) // 2


def solve(n, x, d):
    d = d + d

    ans = 0
    i = 0
    j = 0
    days = 0
    cnt = 0

    while i < 2*n:
        while j < 2*n and days < x:
            days += d[j]
            cnt += nn2(d[j])
            j += 1
        ans = max(ans, cnt - nn2(days - x))
        days -= d[i]
        cnt -= nn2(d[i])
        i += 1

    return ans


def main():
    n, x = ria()
    d = ria()
    print(solve(n, x, d))


if __name__ == '__main__':
    main()
