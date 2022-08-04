import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from bisect import bisect


def main():
    n = ri()
    a = ria()

    t = [a[0]]
    for i in range(1, n):
        j = bisect(t, a[i])
        if j < len(t):
            t[j] = a[i]
        else:
            t.append(a[i])

    wi(len(t))


if __name__ == '__main__':
    main()
