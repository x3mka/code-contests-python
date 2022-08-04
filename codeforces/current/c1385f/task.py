import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k, ee):
    g = [[] for _ in range(n)]
    for e in ee:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])

    leafs = [[] for _ in range(n)]
    for i in range(n):
        if len(g[i]) == 1:
            leafs[g[i][0]].append(i)

    deg = [len(g[i]) for i in range(n)]

    deleted = set()
    ans = 0

    q = [i for i in range(n) if len(leafs[i]) >= k]

    while q:
        v = q.pop()
        if v in deleted:
            continue

        x = len(leafs[v]) // k
        cnt = x * k
        ans += x

        while cnt > 0:
            w = leafs[v].pop()
            deleted.add(w)
            cnt -= 1

        deg[v] -= x * k
        if deg[v] == 1:  # became a leaf
            for w in g[v]:
                if w not in deleted:
                    leafs[w].append(v)
                    if len(leafs[w]) == k:
                        q.append(w)

    return ans


def main():
    for _ in range(ri()):
        n, k = ria()
        e = []
        for i in range(n-1):
            xi, yi = ria()
            xi -= 1
            yi -= 1
            e.append([xi, yi])

        wi(solve(n, k, e))


if __name__ == '__main__':
    main()
