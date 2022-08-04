import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a, b):
    am = min(a)
    bm = min(b)

    cnt = 0
    for i in range(n):
        aim = a[i] - am
        bim = b[i] - bm
        x = min(aim, bim)
        cnt += x
        cnt += aim - x
        cnt += bim - x
    return cnt


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        wi(solve(n, a, b))


if __name__ == '__main__':
    main()
