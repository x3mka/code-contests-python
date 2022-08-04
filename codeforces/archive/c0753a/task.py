def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n):
    k = 1
    while k * (k+1) // 2 <= n:
        k += 1

    ans = k-1
    print(ans)

    a = list(range(1, ans+1))
    left = n - ans * (ans + 1) // 2
    for i in range(left):
        a[ans-i-1] += 1

    print(ia_to_s(a))


def main():
    n = ri()
    solve(n)


if __name__ == '__main__':
    main()
