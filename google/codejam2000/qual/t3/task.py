import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def overlap(a, b):
    return max(0, min(a[1], b[1]) - max(a[0], b[0])) > 0


from collections import deque


def bfs(g, color, v):
    q = deque()
    q.append((v, 0))
    color[v] = 0

    while q:
        v, c = q.popleft()
        for w in g[v]:
            if color[w] == c:
                return False
            if color[w] == -1:
                color[w] = 1 - c
                q.append((w, 1 - c))
    return True


def solve(n, a):
    g = [[] for _ in range(n)]

    d = {}
    for i in range(n):
        seg = a[i]
        if seg[0] not in d:
            d[seg[0]] = [[], []]
        d[seg[0]][0].append(i)
        if seg[1] not in d:
            d[seg[1]] = [[], []]
        d[seg[1]][1].append(i)

    cur = set()
    for x in sorted(d):
        y = d[x]
        for i in y[1]:  # all segments ending here
            cur.remove(i)
        for i in y[0]:  # all segments starting here (they all intersect each segment in cur)
            for j in cur:
                g[i].append(j)
                g[j].append(i)
            cur.add(i)

    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            if not bfs(g, color, i):
                return "IMPOSSIBLE"

    return ''.join(['C' if c == 0 else 'J' for c in color])


def main():
    for t in range(ri()):
        n = ri()
        a = []
        for _ in range(n):
            a.append(tuple(ria()))
        ws("Case #{}: {}".format(t+1, solve(n, a)))


if __name__ == '__main__':
    main()
