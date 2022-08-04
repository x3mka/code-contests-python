import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n, x = ria()
    p = sorted(ria())

    cnt = 0
    i = 0
    j = n-1
    while i <= j:
        c = p[j]
        if c + p[i] <= x:
            c += p[i]
            i += 1
        j -= 1
        cnt += 1

    wi(cnt)


if __name__ == '__main__':
    main()
