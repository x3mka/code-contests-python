def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(a, n, m):
    d = [[0] * m for _ in range(n)]

    prev = a[0][0]
    for j in range(1, m):
        curr = a[0][j]
        if curr > prev:
            delta = curr - prev - 1
            prev = prev + 1
        else:
            delta = prev - curr + 1
            prev = curr - 1
        d[0][j] = d[0][j-1] + delta

    prev = a[0][0]
    for i in range(1, n):
        curr = a[i][0]
        if curr > prev:
            delta = curr - prev - 1
            prev = prev + 1
        else:
            delta = prev - curr + 1
            prev = curr - 1
        d[i][0] = d[i-1][0] + delta

    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = min(d[i-1][j] + abs(a[i-1][j]-a[i][j]+1), d[i][j-1] + abs(a[i-1][j]-a[i][j]+1))

    return d[n-1][m-1]


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for __ in range(n):
            a.append(ria())
        print(solve(a, n, m))


if __name__ == '__main__':
    main()
