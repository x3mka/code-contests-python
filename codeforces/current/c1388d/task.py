import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a, b):
    for i in range(n):
        if b[i] > 0:
            b[i] -= 1

    in_deg = [0] * n

    for i in range(n):
        if b[i] != -1:
            in_deg[b[i]] += 1

    q = [i for i in range(n) if in_deg[i] == 0]

    ans = 0
    res = []
    end = []

    while q:
        v = q.pop()
        if a[v] < 0:
            end.append(v)
        else:
            res.append(v)
            ans += a[v]
            if b[v] != -1:
                a[b[v]] += a[v]

        if b[v] != -1:
            in_deg[b[v]] -= 1
            if in_deg[b[v]] == 0:
                q.append(b[v])

    for v in reversed(end):
        res.append(v)
        ans += a[v]
        if b[v] != -1:
            a[b[v]] += a[v]

    wi(ans)
    wia([i+1 for i in res])


def main():
    n = ri()
    a = ria()
    b = ria()
    solve(n, a, b)


if __name__ == '__main__':
    main()
