import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    cnt = [0] * (2 * n + 1)

    d = {}
    for ai in a:
        if ai not in d:
            d[ai] = 0
        d[ai] += 1

    for s in range(2 * n + 1):
        taken = [False] * n
        dd = d.copy()
        for i in range(n):
            if taken[i]:
                continue
            x = a[i]
            y = s - a[i]
            if x == y:
                if x in dd and dd[x] > 1:
                    cnt[s] += 1
                    dd[x] -= 2
            else:
                if x in dd and dd[x] > 0 and y in dd and dd[y] > 0:
                    cnt[s] += 1
                    dd[x] -= 1
                    dd[y] -= 1

    return max(cnt)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
