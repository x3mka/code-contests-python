import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(x, y, k):
    d = dict()
    c = dict()

    while k > 0:
        if x in d:
            cycle = c[x] - k
            if k >= cycle:
                k %= cycle
                continue
        else:
            d[x] = 0
            c[x] = k

        steps_till_divisible = y - (x % y)
        if k >= steps_till_divisible:
            x += steps_till_divisible
            while x % y == 0:
                x //= y
            k -= steps_till_divisible
        else:
            x += k
            k = 0

    return x


def main():
    for _ in range(ri()):
        x, y, k = ria()
        wi(solve(x, y, k))


if __name__ == '__main__':
    main()
