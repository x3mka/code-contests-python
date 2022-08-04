import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    a = []
    b = []
    for i in range(n):
        s, e = ria()
        a.append(s)
        b.append(e)

    a.sort()
    b.sort()

    best = 0
    c = 0
    i = 0
    j = 0
    while i < n or j < n:
        if i < n and j == n or i < n and a[i] < b[j]:
            i += 1
            c += 1
            best = max(best, c)
        else:
            j += 1
            c -= 1

    wi(best)


if __name__ == '__main__':
    main()
