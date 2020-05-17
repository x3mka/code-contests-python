def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(s, n, k):
    all_ones = 0
    for i in range(n):
        if s[i] == '1':
            all_ones += 1

    res = all_ones
    for i in range(k):
        # subarray max sum in array [i, i+k, i+2k, ..]
        d = 0
        for j in range(i, n, k):
            if s[j] == '1':
                d += 1
            if s[j] == '0':
                d -= 1
            if d < 0:
                d = 0
            res = min(res, all_ones-d)
    return res


def main():
    for _ in range(ri()):
        n, k = ria()
        s = rs()
        print(solve(s, n, k))


if __name__ == '__main__':
    main()
