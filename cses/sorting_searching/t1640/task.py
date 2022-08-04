import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, x = ria()
    a = ria()
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1

    for i in range(n):
        if a[i] + a[i] == x and a[i] in d and d[a[i]] >= 2 or \
           a[i] + a[i] != x and x - a[i] in d:
            for j in range(i+1, n):
                if a[j] == x - a[i]:
                    wia([i+1, j+1])
                    return

    ws('IMPOSSIBLE')


if __name__ == '__main__':
    main()
