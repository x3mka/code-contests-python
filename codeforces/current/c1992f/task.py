import math
import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, x, a):
    ans = 1
    factors = {1}
    for ai in a:
        if x % ai > 0:
            continue

        new_factors = factors.copy()
        for f in factors:
            m = f * ai
            if x % m == 0:
                new_factors.add(m)

        if x in new_factors:
            ans += 1
            factors = {1, ai}
        else:
            factors = new_factors

    return ans


def main():
    for _ in range(ri()):
        n, x = ria()
        a = ria()
        wi(solve(n, x, a))


if __name__ == '__main__':
    main()
