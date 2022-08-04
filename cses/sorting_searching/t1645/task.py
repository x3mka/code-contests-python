import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    a = ria()

    res = []
    b = []

    for i in range(n):
        while len(b) > 0:
            x, y = b[-1]
            if y < a[i]:
                break
            b.pop()

        if len(b) == 0:
            x = 0

        res.append(x)
        b.append((i+1, a[i]))

    wia(res)


if __name__ == '__main__':
    main()
