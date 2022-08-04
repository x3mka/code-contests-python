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

    best = 0
    cur = 0
    cnt = 0
    found = False

    for i in range(n):
        cur += a[i]
        cnt += 1
        if cur <= 0:
            cur = 0
            cnt = 0
        if cnt > 0:
            best = max(best, cur)
            found = True

    if not found:
        best = max(a)

    wi(best)


if __name__ == '__main__':
    main()
