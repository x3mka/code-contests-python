import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    for t in range(ri()):
        a, b = ria()

        if a <= 2*b and b <= 2*a and (a+b)%3 == 0:
            ws('YES')
        else:
            ws('NO')


if __name__ == '__main__':
    main()
