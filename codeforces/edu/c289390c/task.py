import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n

        self.exp = [0] * n

    def get_exp(self, a):
        res = self.exp[a]
        acopy = a
        while acopy != self.parent[acopy]:
            acopy = self.parent[acopy]
        return res

    def add_exp(self, a, val):
        a = self.find(a)
        self.exp[a] += val

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.exp[a] < self.exp[b]:
                a, b = b, a

            self.n -= 1
            self.parent[b] = a
            # self.size[a] += self.size[b]
            # self.exp[a] += self.exp[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.n


def main():
    n, m = ria()

    dsu = DSU(n)
    for i in range(m):
        s = rs()

        if 'add' in s:
            op, a, val = s.split()
            a = int(a) - 1
            val = int(val)
            dsu.add_exp(a, val)

        if 'get' in s:
            op, a = s.split()
            a = int(a) - 1
            wi(dsu.get_exp(a))

        if 'join' in s:
            op, a, b = s.split()
            a = int(a)-1
            b = int(b)-1
            dsu.union(a, b)


if __name__ == '__main__':
    main()
