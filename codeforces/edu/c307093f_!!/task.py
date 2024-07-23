import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import deque


class MinMaxStack:
    def __init__(self, mx=10**18+1, mn=-(10**18+1)):
        self.items = []
        self.mn = deque()
        self.mx = deque()
        self.mn.append(mx)
        self.mx.append(mn)

    def push(self, x):
        self.items.append(x)
        self.mn.append(min(self.mn[-1], x))
        self.mx.append(max(self.mx[-1], x))

    def pop(self):
        if not self.items:
            return
        self.items.pop()
        self.mn.pop()
        self.mx.pop()

    def top(self): return self.items[-1]
    def min(self): return self.mn[-1]
    def max(self): return self.mx[-1]
    def empty(self): return len(self.items) == 0


class MinMaxQueue:
    def __init__(self):
        self.s1 = MinMaxStack()
        self.s2 = MinMaxStack()

    def push(self, x):
        self.s1.push(x)

    def _pour(self):
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.top())
                self.s1.pop()

    def front(self):
        if self.s2.empty():
            self._pour()
        if self.s2.empty():
            return -1
        return self.s2.top()

    def pop(self):
        if self.s2.empty():
            self._pour()
        if not self.s2.empty():
            return self.s2.pop()

    def max(self):
        return max(self.s1.max(), self.s2.max())

    def min(self):
        return min(self.s1.min(), self.s2.min())


def solve(n, k, a):
    # see how recalculate min/max when moving l
    # https://cs.stackexchange.com/questions/93057/given-an-array-of-integers-and-a-value-k-find-the-length-of-the-longest-subarra
    ans = 0
    l = 0
    mmq = MinMaxQueue()
    # mn = deque()
    # mx = deque()
    for r in range(n):
        # while mn and a[mn[-1]] >= a[r]:
        #     mn.pop()
        # mn.append(r)
        # while mx and a[mx[-1]] <= a[r]:
        #     mx.pop()
        # mx.append(r)
        mmq.push(a[r])

        # min_idx = mn[0]
        # min_val = a[min_idx]
        #
        # max_idx = mx[0]
        # max_val = a[max_idx]

        while mmq.max() - mmq.min() > k:
            l += 1
            mmq.pop()

            # if l > min_idx:
            #     mn.popleft()
            # if l > max_idx:
            #     mx.popleft()
            # min_idx = mn[0]
            # min_val = a[min_idx]
            # max_idx = mx[0]
            # max_val = a[max_idx]

        ans += r - l + 1

    return ans


def main():
    n, k = ria()
    a = ria()
    wi(solve(n, k, a))


if __name__ == '__main__':
    main()