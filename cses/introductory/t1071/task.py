import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(r, c):
    if r >= c:
        x = r * r if r % 2 == 0 else (r - 1) * (r - 1) + 1
        if r % 2 == 1:
            x += (c - 1)
        else:
            x -= (c - 1)
    else:
        x = c * c if c % 2 == 1 else (c - 1) * (c - 1) + 1
        if c % 2 == 1:
            x -= (r - 1)
        else:
            x += (r - 1)
    return x


def main():
    for t in range(ri()):
        r, c = ria()
        wi(solve(r, c))


if __name__ == '__main__':
    main()
