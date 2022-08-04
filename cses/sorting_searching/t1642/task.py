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
    if len(a) < 4:
        ws('IMPOSSIBLE')
        return

    b = []

    for i in range(n-1):
        for j in range(i + 1, n):
            b.append((a[i] + a[j], i, j))

    m = len(b)

    d = {}
    for i in range(m):
        if b[i][0] not in d:
            d[b[i][0]] = 0
        d[b[i][0]] += 1

    for i in range(m):
            y = x - b[i][0]
            if y not in d:
                continue
            cnt = d[y]
            if b[i][0] == y:
                cnt -= 1
            if cnt > 0:
                for j in range(m):
                    if j == i:
                        continue
                    if b[j][0] == y and len(set([b[i][1], b[i][2]]).intersection(set([b[j][1], b[j][2]]))) == 0:
                        wia([b[i][1] + 1, b[i][2] + 1, b[j][1] + 1, b[j][2] + 1])
                        return

    ws('IMPOSSIBLE')


if __name__ == '__main__':
    main()
