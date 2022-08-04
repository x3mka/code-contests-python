def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, m, k):
    d = n // k
    d_max = min(m, d)
    left = m - d_max

    dd = left // (k-1)
    if left % (k-1) > 0:
        dd += 1

    return d_max - dd


def main():
    for _ in range(ri()):
        n, m, k = ria()
        print(solve(n, m, k))


if __name__ == '__main__':
    main()
