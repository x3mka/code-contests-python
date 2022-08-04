import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, e0, e1):
    g = [[] for _ in range(n)]
    for e in e1:
        g[e[0]].append(e[1])

    res, found = [], [0] * n
    stack = list(range(n))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += g[node]

    # cycle check
    for node in res:
        if any(found[nei] for nei in g[node]):
            ws('NO')
            return
        found[node] = 0

    topo_sorted = res[::-1]

    idx = [0] * n
    for i in range(n):
        idx[topo_sorted[i]] = i

    ws('YES')
    for e in e1:
        wia([e[0]+1, e[1]+1])

    for e in e0:
        if idx[e[0]] < idx[e[1]]:
            wia([e[0]+1, e[1]+1])
        else:
            wia([e[1]+1, e[0]+1])


def main():
    for _ in range(ri()):
        n, m = ria()
        e0 = []
        e1 = []
        for i in range(m):
            ti, xi, yi = ria()
            xi -= 1
            yi -= 1
            if ti == 0:
                e0.append((xi, yi))
            else:
                e1.append((xi, yi))

        solve(n, m, e0, e1)


if __name__ == '__main__':
    main()
