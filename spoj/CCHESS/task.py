import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


import heapq


def solve1(a, b, c, d):
    """Dijkstra"""
    inf = 10**9
    dist = [[inf] * 8 for _ in range(8)]
    dist[a][b] = 0

    pq = [(0, a, b)]

    idx = [-2, -2, -1, 1, 2, 2, 1, -1]
    idy = [-1, 1, 2, 2, 1, -1, -2, -2]

    while pq:
        _, x, y = heapq.heappop(pq)

        for i in range(8):
            xx = x + idx[i]
            yy = y + idy[i]
            if xx < 0 or xx > 7 or yy < 0 or yy > 7:
                continue
            if dist[x][y] + x * xx + y * yy < dist[xx][yy]:
                dist[xx][yy] = dist[x][y] + x * xx + y * yy
                heapq.heappush(pq, (dist[xx][yy], xx, yy))

    return dist[c][d]


def pre_calc():
    """Floyd-Warshall"""
    n = 8
    idx = [-2, -2, -1, 1, 2, 2, 1, -1]
    idy = [-1, 1, 2, 2, 1, -1, -2, -2]

    edges = []

    key = lambda x, y: y * n + x
    dst = lambda x, y, xx, yy: x * xx + y * yy

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ii = i + idx[k]
                jj = j + idy[k]
                if ii < 0 or ii > n-1 or jj < 0 or jj > n-1:
                    continue
                edges.append((key(i, j), key(ii, jj), dst(i, j, ii, jj)))

    nn = n * n
    dist = [[0 if i == j else float("inf") for i in range(nn)] for j in range(nn)]

    for u, v, dd in edges:
        dist[u][v] = dd

    for k in range(nn):
        for i in range(nn):
            for j in range(nn):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def main():
    dist = pre_calc()
    key = lambda x, y: y * 8 + x
    for line in sys.stdin:
        a, b, c, d = list(map(int, line.split()))
        wi(dist[key(a, b)][key(c, d)])


if __name__ == '__main__':
    main()
