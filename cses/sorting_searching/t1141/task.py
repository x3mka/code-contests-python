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
    s = set()
    l = 0
    for r in range(n):
        if a[r] not in s:
            s.add(a[r])
            best = max(best, len(s))
        else:
            while a[l] != a[r]:
                s.remove(a[l])
                l += 1
            l += 1

    wi(best)


if __name__ == '__main__':
    main()
