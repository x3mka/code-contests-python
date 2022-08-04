def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(a1, k):
    res = a1
    for _ in range(k-1):
        a = [int(x) for x in str(res)]
        min_d = min(a)
        max_d = max(a)
        if min_d == 0:
            return res
        res += min_d * max_d
    return res


def main():
    for _ in range(ri()):
        a1, k = ria()
        print(solve(a1, k))


if __name__ == '__main__':
    main()
