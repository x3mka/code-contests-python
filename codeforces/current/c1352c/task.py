def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n, k):
    m = k // (n-1)
    return m * n - 1 if k == m * (n-1) else m * n + (k - m * (n-1))


def main():
    for _ in range(ri()):
        n, k = ria()
        print(solve(n, k))


if __name__ == '__main__':
    main()
