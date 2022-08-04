def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n, k):
    if n < k:
        return []
    if n == k:
        return [1] * k

    # n > k

    if n % 2 == 0:
        if n >= 2*k:
            return [2] * (k-1) + [n - 2*(k-1)]
        else:
            if k % 2 == 0:
                return [1] * (k - 1) + [n - k + 1]
            else:
                return []
    else:
        #only odds
        if k % 2 == 0:
            return []
        else:
            return [1] * (k-1) + [n-k+1]


def main():
    for _ in range(ri()):
        n, k = ria()
        a = solve(n, k)
        if len(a) > 0:
            print('YES')
            print(ia_to_s(a))
        else:
            print("NO")


if __name__ == '__main__':
    main()
