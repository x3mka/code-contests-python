import sys


def rs(): return input().strip()
def ri(): return int(input())
# def ria(): return list(map(int, input().split()))
def ria(): return list(map(int, sys.stdin.readline().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


import heapq


class Group(object):
    def __init__(self, data=None):
        self.size = 0 if data is None else len(data)
        self.e = 0 if data is None else max(data)

    def __repr__(self):
        return f'Group: e={self.e}, len={self.size})'

    def is_ok(self):
        return self.size > 0 and self.size >= self.e

    def __lt__(self, other):
        this_p = self.e - self.size
        other_p = other.e - other.size
        return this_p < other_p

    def union(self, other):
        self.size += other.size
        self.e = max(self.e, other.e)


def solve(n, e):
    groups = [Group([ei]) for ei in e]
    heapq.heapify(groups)

    res = 0
    while len(groups) > 0:
        cg = Group()
        while not cg.is_ok() and len(groups) > 0:
            g = heapq.heappop(groups)
            cg.union(g)
        if cg.is_ok():
            res += 1

    return res


def main():
    for _ in range(ri()):
        n = ri()
        e = ria()
        print(solve(n, e))


if __name__ == '__main__':
    main()
