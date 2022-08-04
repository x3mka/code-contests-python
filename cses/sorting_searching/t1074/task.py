import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    """This is ternary search. But there is an easier solution: target length is a median in a sorted array of sticks lengths"""
    n = ri()
    p = ria()

    lo = min(p)
    hi = max(p)

    def f(x):
        return -sum([abs(x - pi) for pi in p])

    while lo < hi:
        mid = (hi + lo) >> 1
        if f(mid) > f(mid + 1):
            hi = mid
        else:
            lo = mid + 1

    wi(-f(lo))


if __name__ == '__main__':
    main()
