import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = 7
    path = rs()
    ways = 'DULR'

    visited = [[False]*n for _ in range(n)]

    def possible(x, y, move):
        if x == 0 and move == 'U':
            return False
        if x == n-1 and move == 'D':
            return False
        if y == 0 and move == 'L':
            return False
        if y == n-1 and move == 'R':
            return False
        return True

    def go(start, x, y):
        if start == n * n - 1:
            return 1 if x == n-1 and y == 0 else 0
        if x == n - 1 and y == 0:
            return 0

        # if you hit a wall or a path (can only go left or right); return
        if (((x + 1 == n or (x > 0 and x + 1 < n and visited[x - 1][y] and visited[x + 1][y])) and y - 1 >= 0 and y + 1 < n and not visited[x][y - 1] and not visited[x][y + 1]) or
            ((y + 1 == n or (y > 0 and y + 1 < n and visited[x][y - 1] and visited[x][y + 1])) and x - 1 >= 0 and x + 1 < n and not visited[x - 1][y] and not visited[x + 1][y]) or
            ((x == 0 or (x > 0 and x + 1 < n and visited[x + 1][y] and visited[x - 1][y])) and y - 1 >= 0 and y + 1 < n and not visited[x][y - 1] and not visited[x][y + 1]) or
            ((y == 0 or (y > 0 and y + 1 < n and visited[x][y + 1] and visited[x][y - 1])) and x - 1 >= 0 and x + 1 < n and not visited[x - 1][y] and not visited[x + 1][y])):
            return 0

        res = 0

        moves = ways if path[start] == '?' else [path[start]]
        for move in moves:
            if not possible(x, y, move):
                if len(moves) > 1:
                    continue
                else:
                    return 0
            nx, ny = x, y
            if move == 'U':
                nx -= 1
            if move == 'D':
                nx += 1
            if move == 'L':
                ny -= 1
            if move == 'R':
                ny += 1
            if visited[nx][ny]:
                if len(moves) > 1:
                    continue
                else:
                    return 0

            visited[nx][ny] = True
            mms.append(move)
            res += go(start + 1, nx, ny)
            mms.pop()
            visited[nx][ny] = False
        return res

    mms = []
    visited[0][0] = True
    wi(go(0, 0, 0))


if __name__ == '__main__':
    main()
