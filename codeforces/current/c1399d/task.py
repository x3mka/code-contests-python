import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s):
    res = []
    cnt = 1
    g0 = {1}
    g1 = {1}

    for i in range(n):
        if s[i] == '0':
            if len(g1) == 0:
                cnt += 1
                g1.add(cnt)
            g = next(iter(g1))
            res.append(g)
            g1.remove(g)
            g0.add(g)

        else:
            if len(g0) == 0:
                cnt += 1
                g0.add(cnt)
            g = next(iter(g0))
            res.append(g)
            g0.remove(g)
            g1.add(g)

    wi(cnt)
    wia(res)


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        solve(n, s)


if __name__ == '__main__':
    main()
