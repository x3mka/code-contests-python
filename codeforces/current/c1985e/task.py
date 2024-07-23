import math
import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(x, y, z, k):
    divs = []
    for d in range(1, 2001):
        if k % d == 0:
            divs.append(d)

    x_less = [f for f in divs if f <= x]
    y_less = [f for f in divs if f <= y]
    z_less = [f for f in divs if f <= z]

    ans = 0

    for sx in x_less:
        for sy in y_less:
            for sz in z_less:
                if sx * sy * sz == k:
                    ans = max(ans, (x - sx + 1) * (y - sy + 1) * (z - sz + 1))

    return ans


def main():
    for _ in range(ri()):
        x, y, z, k = ria()
        wi(solve(x, y, z, k))


if __name__ == '__main__':
    main()
