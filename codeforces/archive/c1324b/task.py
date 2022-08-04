def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, a):
    d = {}
    for i in range(0, n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    left = {a[0]: 1}
    for i in range(1, n-1):
        d[a[i]] -= 1
        for k in left.keys():
            if k in d and d[k] > 0:
                return True
    return False


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        print('YES' if solve(n, a) else 'NO')


if __name__ == '__main__':
    main()
