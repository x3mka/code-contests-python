def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, a):
    even_count = sum([1 for x in a if x % 2 == 0])
    if even_count % 2 == 0:
        return True

    a = sorted(a)

    for i in range(1, n):
        if abs(a[i]-a[i-1]) == 1:
            return True

    return False


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        print('YES' if solve(n, a) else 'NO')


if __name__ == '__main__':
    main()
