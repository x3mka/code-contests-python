import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import math


class SparseTable:

    def __init__(self, data):
        self._n = n = len(data)
        self._k = k = int(math.log2(n))+1
        self.data = data
        self.st = [[0] * k for _ in range(n)]

        for i in range(n):
            self.st[i][0] = data[i]

        j = 1
        while (1 << j) <= n:
            i = 0
            while (i + (1 << j) - 1) < n:
                if (self.st[i][j - 1] <
                        self.st[i + (1 << (j - 1))][j - 1]):
                    self.st[i][j] = self.st[i][j - 1]
                else:
                    self.st[i][j] = self.st[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self, l, r):
        j = int(math.log2(r - l + 1))
        if self.st[l][j] <= self.st[r - (1 << j) + 1][j]:
            return self.st[l][j]
        else:
            return self.st[r - (1 << j) + 1][j]

    def __repr__(self):
        return "SparseTable({0})".format(self.st)


def main():
    n, a, b = ria()
    x = ria()

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + x[i]

    st = SparseTable(pre)

    best = -float('inf')
    for r in range(a, n + 1):
        mn = st.query(max(0, r - b), r - a)
        best = max(best, pre[r] - mn)

    wi(best)


if __name__ == '__main__':
    main()
