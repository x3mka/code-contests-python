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
            d[a[i]] = 0
        d[a[i]] += 1

    for i in range(n-1):
        for j in range(i+1, n):
            y = x - a[i] - a[j]
            if y not in d:
                continue
            cnt = d[y]
            if a[i] == y:
                cnt -= 1
            if a[j] == y:
                cnt -= 1
            if cnt > 0:
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if a[k] == y:
                        wia([i+1, j+1, k+1])
                        return

    ws('IMPOSSIBLE')


if __name__ == '__main__':
    main()
