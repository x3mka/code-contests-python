import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a])); sys.stdout.write('\n')


import math


def solve(n, k, a):
    h = [a[i+1] - a[i] for i in range(n-1)]
    m = max(h)
    left = 1
    right = m
    while right > left:
        mid = (left + right) // 2
        kk = sum([math.ceil(hi / mid)-1 for hi in h])
        if kk > k:
            left = mid+1
        else:
            right = mid
    return left


def main():
    for t in range(ri()):
        n, k = ria()
        a = ria()
        ws("Case #{}: {}".format(t+1, solve(n, k, a)))


if __name__ == '__main__':
    main()
