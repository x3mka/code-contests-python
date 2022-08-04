import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    if n == 1 or n == 2:
        ws('NO')
        return

    a = [i+1 for i in range(n)]
    s = sum(a)
    if s % 2 == 1:
        ws('NO')
        return

    t = s // 2
    s1 = []
    s2 = []
    c = 0
    for i in range(n-1, -1, -1):
        if c + a[i] <= t:
            s1.append(a[i])
            c += a[i]
        else:
            s2.append(a[i])

    ws('YES')
    wi(len(s1))
    wia(s1)
    wi(len(s2))
    wia(s2)


if __name__ == '__main__':
    main()
