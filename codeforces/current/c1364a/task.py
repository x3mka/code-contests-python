import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from itertools import permutations, combinations


def solve(n, x, a):
    # n = 6
    # a = [i+1 for i in range(n)]
    #
    # for p in list(permutations(a)):
    #     best = 0
    #     best_c = ()
    #     for k in range(2, n-1):
    #         for c in combinations(p, k):
    #             s = 0
    #             for i in range(k-1):
    #                 s += abs(c[i]-c[i+1])
    #             if s > best:
    #                 best = s
    #                 best_c = c
    #     wia(p)
    #     ws("Best: {0}, {1}".format(best, best_c))
    # return


    if sum([1 for ai in a if ai % x == 0]) == n:
        return -1

    s = sum(a)
    if s % x > 0:
        return n

    mm = n + 1
    left = mm
    right = mm
    for i in range(n):
        if left == mm and a[i] % x > 0:
            left = i
        if right == mm and a[n-i-1] % x > 0:
            right = i
    return n - min(left+1, right+1)


def main():
    for _ in range(ri()):
        n, x = ria()
        a = ria()
        wi(solve(n, x, a))


if __name__ == '__main__':
    main()
