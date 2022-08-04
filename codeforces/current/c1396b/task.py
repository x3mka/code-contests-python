import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import deque


def main():
    n, m, x, y = ria()
    x -= 1
    y -= 1
    res = []
    v = [[False] * m for _ in range(n)]

    res.append((x, y))
    v[x][y] = True

    def fill_row(r, c):
        if not v[r][c]:
            res.append((r, c))
            v[r][c] = True
        to_visit = set([j for j in range(1, m-1) if not v[r][j]])
        if len(to_visit) == 0:
            if not v[r+1][c]:
                return r+1, c
            else:
                return r+2, c

        out_col = None
        for out_col in to_visit:
            if not v[r+1][out_col]:
                break

        to_visit.remove(out_col)
        for c in to_visit:
            res.append((r, c))
            v[r][c] = True
        if not v[r][out_col]:
            res.append((r, out_col))
            v[r][out_col] = True
        return r+1, out_col

    r = 1
    c = y
    while r < n-1:
        r, c = fill_row(r, c)

    res.append((n-1, c))
    v[n-1][c] = True

    q = deque([(n-1, c-1)])
    while q:
        r, c = q.popleft()
        res.append((r, c))
        v[r][c] = True

        if r > 0 and not v[r-1][c]:
            q.append((r-1, c))
        if r < n-1 and not v[r+1][c]:
            q.append((r+1, c))
        if c > 0 and not v[r][c-1]:
            q.append((r, c-1))
        if c < m-1 and not v[r][c+1]:
            q.append((r, c+1))

    for r in res:
        wia([r[0]+1, r[1]+1])


if __name__ == '__main__':
    main()
