def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


import heapq


class Range(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Range: [{self.left},{self.right})'

    def __lt__(self, other):
        this_len = self.right-self.left
        other_len = other.right-other.left

        if this_len == other_len:
            return self.left < other.left
        else:
            return this_len > other_len


def solve(n):
    a = [0] * n
    ranges = [Range(0, n)]
    heapq.heapify(ranges)

    iteration = 1
    while len(ranges) > 0:
        r = heapq.heappop(ranges)
        i = (r.left + r.right - 1) // 2
        a[i] = iteration
        if i > r.left:
            heapq.heappush(ranges, Range(r.left,i))
        if r.right > (i+1):
            heapq.heappush(ranges, Range(i+1, r.right))
        iteration += 1

    return a


def main():
    for _ in range(ri()):
        n = ri()
        print(ia_to_s(solve(n)))


if __name__ == '__main__':
    main()
