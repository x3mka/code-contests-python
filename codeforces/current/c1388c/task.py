import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import deque


def toposort(graph):
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


def solve(n, m, p, h, e):
    order = []
    pre = [-1] * n

    visited = [False] * n
    q = deque([0])

    while q:
        v = q.popleft()
        order.append(v)
        visited[v] = True
        for w in e[v]:
            if not visited[w]:
                q.append(w)
                pre[w] = v

    past = [0] * n
    bvs = [0] * n

    for v in reversed(order):
        past[v] = p[v]
        for w in e[v]:
            if w == pre[v]:
                continue
            past[v] += past[w]

        mv = past[v]
        gv = (mv + h[v]) / 2
        bv = (mv - h[v]) / 2

        if gv < 0 or bv < 0 or int(gv) != gv or int(bv) != bv:
            ws('NO')
            return

        bvs[v] = int(bv)
        cnt = 0
        for w in e[v]:
            if w == pre[v]:
                continue
            cnt += bvs[w]
        # down = past[v] - p[v]
        if cnt < bvs[v] - p[v]:
            ws('NO')
            return

        if v == 0 and mv != m:
            ws('NO')
            return

    ws('YES')


def main():
    for _ in range(ri()):
        n, m = ria()
        p = ria()
        h = ria()
        e = [[] for i in range(n)]
        for i in range(n - 1):
            x, y = ria()
            x -= 1
            y -= 1
            e[x].append(y)
            e[y].append(x)
        solve(n, m, p, h, e)


if __name__ == '__main__':
    main()
