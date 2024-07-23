import math
import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')




from collections import deque


class GcdStack:
    def __init__(self):
        self.items = []
        self._gcd = deque()
        self._gcd.append(0)

    def push(self, x):
        self.items.append(x)
        self._gcd.append(math.gcd(self._gcd[-1], x))

    def pop(self):
        if not self.items:
            return
        self.items.pop()
        self._gcd.pop()

    def top(self): return self.items[-1]
    def gcd(self): return self._gcd[-1]
    def empty(self): return len(self.items) == 0


class GcdQueue:
    def __init__(self):
        self.s1 = GcdStack()
        self.s2 = GcdStack()

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

    def gcd(self):
        return math.gcd(self.s1.gcd(), self.s2.gcd())





# can be solved by bin search over min segment length ?
# similar idea: https://discuss.codechef.com/t/max-subarray-gcd-editorial/11921

# def solve1(n, a):
#     if math.gcd(a) > 1:
#         return -1
#     lo = 0
#     hi = n
#     while hi - lo > 1:
#         mid = (hi + lo) // 2
#         blocks = math.ceil(n / mid)
#
#     return lo + 1



def solve(n, a):
    ans = sys.maxsize
    l = 0
    gcd_q = GcdQueue()
    for r in range(n):
        gcd_q.push(a[r])
        while gcd_q.gcd() == 1:
            ans = min(ans, r - l + 1)
            l += 1
            gcd_q.pop()

    return -1 if ans == sys.maxsize else ans


def main():
    n = ri()
    a = ria()
    wi(solve(n, a))


if __name__ == '__main__':
    main()