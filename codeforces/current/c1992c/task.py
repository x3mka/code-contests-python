import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from itertools import permutations


def get_score(a, n, m, k):
    ans = 0

    fs = 0
    gs = 0
    s = 0
    for i in range(n):
        fs += a[i] if a[i] >= k else 0
        gs += a[i] if a[i] <= m else 0
        s += fs - gs
    if s > ans:
        ans = s
    return ans

def solve(n, m, k):
    # a = [n-i for i in range(n)]  # reversed permutation
    # a = a[:n-m] + list(reversed(a[n-m:]))
    # return a

    start = [n-i for i in range(n-k+1)]
    end = [i+1 for i in range(m)]
    middle = [m+i//2+1 if i % 2 == 0 else k-(i+1)//2 for i in range(k - m - 1)]

    a = start + middle + end
    # score = get_score(a, n, m, k)
    return a

    # a = [n-i for i in range(n)]
    # score = get_score(a, n, m, k)
    # s1 = get_score([5, 3, 4, 1, 2], 5, 2, 5)
    # s2 = get_score([3, 2, 1], 3, 1, 3)
    # s3 = get_score([10, 9, 8, 4, 7, 5, 6, 1, 2, 3], 10, 3, 8)


def main():
    for _ in range(ri()):
        n, m, k = ria()
        wia(solve(n, m, k))


if __name__ == '__main__':
    main()
