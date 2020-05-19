def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def overlap(min1, max1, min2, max2):
    return max(0, min(max1, max2) - max(min1, min2) + 1)


def ok(a,b,c):
    return a+b > c and a+c > b and b+c > a


def naive_solve(A, B, C, D):
    res = 0
    for a in range(A, B+1):
        for y in range(C, D+1):
            res += max(C - max(y-a, B), 0)
    return res


def solve(A, B, C, D):
    # sum(y=[C,D]){ max(C - max(y-a, B), 0) }
    res = 0
    for a in range(A, B+1):
        aB = a + B
        if aB < C:
            #  main sum in [C,D] range
            top = min(a + C, D)
            res += (a + C) * (top - C + 1) - (C + top) * (top - C + 1) // 2
        elif aB > D:
            # sum in [C,D] range of (C-B+1)
            res += (D-C+1)*(C-B+1)
        else:
            # main sum in [C, aB-1] range
            top = min(a + C, aB-1)
            res += (a + C) * (top - C + 1) - (C + top) * (top - C + 1) // 2
            # sum in [aB, D] range of (C-B+1)
            res += (D-aB+1)*(C-B+1)
    return res


def main():
    A, B, C, D = ria()
    print(naive_solve(A, B, C, D))


if __name__ == '__main__':
    main()
