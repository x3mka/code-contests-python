import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import math


def solve(m, d, w):
    mn = min(m, d)
    s = w // math.gcd(d-1, w)

    # find all pairs of numbers in [1, mn] range having the same remainder modulo s
    # x - y == 0 mod s
    # x == y mod s
    k = mn // s
    ans = mn * k - s * (k * (k + 1) // 2)

    return ans


def main():
    for _ in range(ri()):
        m, d, w = ria()
        wi(solve(m, d, w))


if __name__ == '__main__':
    main()
