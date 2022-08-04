import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    d = {}
    for ai in a:
        if ai not in d:
            d[ai] = 0
        d[ai] += 1

    c = []
    i = 0
    while len(c) < n:
        if i not in d:
            c.append(i)
        i += 1

    b = [0] * n

    k = 0
    for i in range(n):
        if i == 0:
            b[i] = c[k]
            k += 1
        else:
            if a[i] != a[i-1]:
                b[i] = a[i-1]
            else:
                b[i] = c[k]
                k += 1

    return b


def main():
    n = ri()
    a = ria()
    res = solve(n, a)
    if res == -1:
        wi(-1)
    else:
        wia(res)


if __name__ == '__main__':
    main()
