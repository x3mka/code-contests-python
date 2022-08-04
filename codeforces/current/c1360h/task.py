def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def how_many(m, a, pre, j):
    return 2**(m-1-j) - sum([1 for x in a if x.startswith(pre) and x[j] == '0'])


def solve(n, m, a):
    k = (2**m-n+1) // 2
    s = ''
    for j in range(m):
        x = how_many(m, a, s, j)
        if x >= k:
            s += '0'
        else:
            s += '1'
            k -= x

    return s


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for __ in range(n):
            a.append(rs())
        print(solve(n, m, a))


if __name__ == '__main__':
    main()
