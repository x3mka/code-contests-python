import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')





from collections import deque


def solve(n, m, a):
    good = []
    bad = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'G':
                good.append((i, j))
            if a[i][j] == 'B':
                bad.append((i, j))

    end_i = n-1
    end_j = m-1

    id_i = [-1, 0, 1, 0]
    id_j = [0, 1, 0, -1]

    ok = lambda x, y: x >= 0 and x < n and y >= 0 and y < m

    for bi, bj in bad:
        for k in range(4):
            bii = bi+id_i[k]
            bjj = bj+id_j[k]
            if not ok(bii, bjj):
                continue
            # if bii == end_i and bjj == end_j:
            #     return False
            for gi, gj in good:
                if bii == gi and bjj == gj:
                    return False
            a[bii][bjj] = '#'

    cnt = 0
    visited = [[False] * m for _ in range(n)]

    if a[end_i][end_j] == '#' and len(good) > 0:
        return False

    q = deque()
    q.append((end_i, end_j))
    visited[end_i][end_j] = True

    while q:
        vi, vj = q.popleft()
        if a[vi][vj] == 'G':
            cnt += 1
        for k in range(4):
            vii = vi + id_i[k]
            vjj = vj + id_j[k]
            if not ok(vii, vjj):
                continue

            if a[vii][vjj] != '#' and not visited[vii][vjj]:
                q.append((vii, vjj))
                visited[vii][vjj] = True

    return cnt == len(good)


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for _ in range(n):
            a.append([si for si in rs()])
        wi('Yes' if solve(n, m, a) else 'No')


if __name__ == '__main__':
    main()
