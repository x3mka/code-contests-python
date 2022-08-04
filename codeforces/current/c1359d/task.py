def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])

# trying to find max subarray sum s with max element = i
def solve(n, a):
    ans = 0
    for i in range(31):
        s = 0
        for j in a:
            if j <= i:
                s = max(0, s + j)
            else:
                s = 0
            ans = max(ans, s - i)

    return ans


def main():
    n = ri()
    a = ria()
    print(solve(n, a))


if __name__ == '__main__':
    main()
