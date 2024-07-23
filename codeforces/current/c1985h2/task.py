import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solve(n, m, a):
    # failed on time on the 21st test

    seen = [[False] * m for i in range(n)]
    r_ones = [0] * n
    c_ones = [0] * m
    r_touch = [0] * n
    c_touch = [0] * m
    rc_touch = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if seen[i][j] or not a[i][j]:
                continue

            size = 0

            q = [(i, j)]
            seen[i][j] = True

            mn_x = i
            mx_x = i
            mn_y = j
            mx_y = j

            while q:
                x, y = q.pop()
                size += 1

                mn_x = min(mn_x, x)
                mx_x = max(mx_x, x)
                mn_y = min(mn_y, y)
                mx_y = max(mx_y, y)

                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] and not seen[nx][ny]:
                        q.append((nx, ny))
                        seen[nx][ny] = True

                r_ones[x] += 1
                c_ones[y] += 1

            # 2-d diffing
            # https://codeforces.com/edu/course/3/lesson/10/4

            r_touch[max(0, mn_x - 1)] += size
            c_touch[max(0, mn_y - 1)] += size
            rc_touch[max(0, mn_x - 1)][max(0, mn_y - 1)] += size

            if mx_x + 2 < n:
                r_touch[mx_x + 2] -= size
                rc_touch[mx_x + 2][max(0, mn_y - 1)] -= size
            if mx_y + 2 < m:
                c_touch[mx_y + 2] -= size
                rc_touch[max(0, mn_x - 1)][mx_y + 2] -= size
            if mx_x + 2 < n and mx_y + 2 < m:
                rc_touch[mx_x + 2][mx_y + 2] += size

            # for x in range(max(0, mn_x - 1), min(n, mx_x + 2)):
            #     r_touch[x] += size
            #     for y in range(max(0, mn_y - 1), min(m, mx_y + 2)):
            #         rc_touch[x][y] += size
            # for y in range(max(0, mn_y - 1), min(m, mx_y + 2)):
            #     c_touch[y] += size

    ans = 1
    for i in range(n):
        r_touch[i] += r_touch[i-1] if i > 0 else 0
        for j in range(m):
            if i == 0 and j > 0:
                c_touch[j] += c_touch[j - 1]
            rc_touch[i][j] += (
                            (i > 0) * rc_touch[i - 1][j] +
                            (j > 0) * rc_touch[i][j - 1] -
                            (i > 0 and j > 0) * (rc_touch[i - 1][j - 1])
            )
            size = r_touch[i] + c_touch[j] - rc_touch[i][j] + n + m - r_ones[i] - c_ones[j] - (0 if a[i][j] else 1)
            ans = max(ans, size)

    return ans


import os
from io import IOBase, BytesIO


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")




def main():
    for _ in range(ri()):
        n, m = ria()

        a = [[] for i in range(n)]
        for i in range(n):
            a[i] = [c == "#" for c in rs()]
        wi(solve(n, m, a))

        # wi(solve1(n, m, a))


if __name__ == '__main__':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    main()
