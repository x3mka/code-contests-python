from math import inf
from sys import stdin

import sys, os, io
read = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class FastIO:
    def __init__(self):
        self.random_seed = 0
        self.flush = False
        self.inf = 1 << 32
        return

    @staticmethod
    def read_int():
        return int(read())

    @staticmethod
    def read_float():
        return float(read())

    @staticmethod
    def read_list_ints():
        return list(map(int, read().split()))

    @staticmethod
    def read_list_ints_minus_one():
        return list(map(lambda x: int(x) - 1, read().split()))

    @staticmethod
    def read_str():
        return read()

    @staticmethod
    def read_list_strs():
        return read().split()

    def get_random_seed(self):
        import random
        self.random_seed = random.randint(0, 10 ** 9 + 7)
        return

    def st(self, x):
        return print(x, flush=self.flush)

    def yes(self, s=None):
        self.st("Yes" if not s else s)
        return

    def no(self, s=None):
        self.st("No" if not s else s)
        return

    def lst(self, x):
        return print(*x, flush=self.flush)

    def flatten(self, lst):
        self.st("\n".join(str(x) for x in lst))
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def ceil(a, b):
        return a // b + int(a % b != 0)

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre


class PointSetRangeMax:

    def __init__(self, n, initial=0):
        self.n = n
        self.initial = initial
        self.cover = [initial] * (4 * n)
        return

    @classmethod
    def merge(cls, x, y):
        return x if x > y else y

    def _push_up(self, i):
        self.cover[i] = self.merge(self.cover[i << 1], self.cover[(i << 1) | 1])
        return

    def build(self, nums):
        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = nums[s]
                else:
                    stack.append((s, t, ~i))
                    m = s + (t - s) // 2
                    stack.append((s, m, i << 1))
                    stack.append((m + 1, t, (i << 1) | 1))
            else:
                i = ~i
                self._push_up(i)
        return

    def get(self):
        stack = [(0, self.n - 1, 1)]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                val = self.cover[i]
                nums[s] = val
                continue
            m = s + (t - s) // 2
            stack.append((s, m, i << 1))
            stack.append((m + 1, t, (i << 1) | 1))
        return nums

    def point_set(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while True:
            if s == t == ind:
                self.cover[i] = val
                break
            m = s + (t - s) // 2
            if ind <= m:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        while i > 1:
            i //= 2
            self._push_up(i)
        return

    def range_max(self, left, right):
        stack = [(0, self.n - 1, 1)]
        ans = self.initial
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans = self.merge(ans, self.cover[i])
                continue
            m = s + (t - s) // 2
            if left <= m:
                stack.append((s, m, i << 1))
            if right > m:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def range_max_bisect_left(self, left, right, val):
        stack = [(0, self.n - 1, 1)]
        res = -1
        while stack and res == -1:
            s, t, i = stack.pop()
            if s == t:
                if left <= s <= right and self.cover[i] >= val:
                    res = s
                continue
            m = s + (t - s) // 2
            if right > m and self.cover[(i << 1) | 1] >= val:
                stack.append((m + 1, t, (i << 1) | 1))
            if left <= m and self.cover[i << 1] >= val:
                stack.append((s, m, i << 1))
        return res


class BinarySearch:
    def __init__(self):
        return

    @staticmethod
    def find_int_left(low: int, high: int, check) -> int:
        """find the minimum int x which make check true"""
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                high = mid
            else:
                low = mid
        return low if check(low) else high

    @staticmethod
    def find_int_left_strictly(low: int, high: int, check) -> int:
        """find the minimum int x which make check true"""
        while low < high:
            mid = low + (high - low) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low

    @staticmethod
    def find_int_right(low: int, high: int, check) -> int:
        """find the maximum int x which make check true"""
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                low = mid
            else:
                high = mid
        return high if check(high) else low

    @staticmethod
    def find_int_right_strictly(low: int, high: int, check) -> int:
        """find the maximum int x which make check true"""
        while low < high:
            mid = low + (high - low + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid - 1
        return high

    @staticmethod
    def find_float_left(low: float, high: float, check, error=1e-6) -> float:
        """find the minimum float x which make check true"""
        while low < high - error:
            mid = low + (high - low) / 2
            if check(mid):
                high = mid
            else:
                low = mid
        return low if check(low) else high

    @staticmethod
    def find_float_right(low: float, high: float, check, error=1e-6) -> float:
        """find the maximum float x which make check true"""
        while low < high - error:
            mid = low + (high - low) / 2
            if check(mid):
                low = mid
            else:
                high = mid
        return high if check(high) else low


class PointSetRangeMin:

    def __init__(self, n, initial=inf):
        self.n = n
        self.initial = initial
        self.cover = [initial] * (4 * n)
        return

    def _make_tag(self, i, val):
        self.cover[i] = val
        return

    def _push_up(self, i):
        self.cover[i] = min(self.cover[i << 1], self.cover[(i << 1) | 1])
        return

    def build(self, nums):

        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self._make_tag(i, nums[s])
                else:
                    stack.append((s, t, ~i))
                    m = s + (t - s) // 2
                    stack.append((s, m, i << 1))
                    stack.append((m + 1, t, (i << 1) | 1))
            else:
                i = ~i
                self._push_up(i)
        return

    def get(self):
        stack = [(0, self.n - 1, 1)]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                val = self.cover[i]
                nums[s] = val
                continue
            m = s + (t - s) // 2
            stack.append((s, m, i << 1))
            stack.append((m + 1, t, (i << 1) | 1))
        return nums

    def point_set(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while True:
            if s == t == ind:
                self._make_tag(i, val)
                break
            m = s + (t - s) // 2
            if ind <= m:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        while i > 1:
            i //= 2
            self._push_up(i)
        return

    def range_min(self, left, right):
        stack = [(0, self.n - 1, 1)]
        ans = self.initial
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans = min(ans, self.cover[i])
                continue
            m = s + (t - s) // 2
            if left <= m:
                stack.append((s, m, i << 1))
            if right > m:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def range_min_bisect_left(self, left, right, val):
        stack = [(0, self.n - 1, 1)]
        res = -1
        while stack and res == -1:
            a, b, i = stack.pop()
            if a == b:
                if left <= a <= right and self.cover[i] <= val:
                    res = a
                continue
            m = a + (b - a) // 2
            if m + 1 <= right and self.cover[(i << 1) | 1] <= val:
                stack.append((m + 1, b, (i << 1) | 1))
            if left <= m and self.cover[i << 1] <= val:
                stack.append((a, m, i << 1))
        return res


class PointSetPreMinPostMin:

    def __init__(self, n, initial=inf):
        self.n = n
        self.initial = initial
        self.pre = [initial] * (4 * n)
        self.post = [initial] * (4 * n)
        return

    def _make_tag(self, i, val):
        self.pre[i] = val
        self.post[i] = val
        return

    def _push_up(self, i):
        self.pre[i] = min(self.pre[i << 1], self.pre[(i << 1) | 1])
        self.post[i] = min(self.post[i << 1], self.post[(i << 1) | 1])
        return

    def build(self, nums):

        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self._make_tag(i, nums[s])
                else:
                    stack.append((s, t, ~i))
                    m = s + (t - s) // 2
                    stack.append((s, m, i << 1))
                    stack.append((m + 1, t, (i << 1) | 1))
            else:
                i = ~i
                self._push_up(i)
        return

    def get(self):
        stack = [(0, self.n - 1, 1)]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                val = self.pre[i]
                nums[s] = val
                continue
            m = s + (t - s) // 2
            stack.append((s, m, i << 1))
            stack.append((m + 1, t, (i << 1) | 1))
        return nums

    def point_set(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while True:
            if s == t == ind:
                self._make_tag(i, val)
                break
            m = s + (t - s) // 2
            if ind <= m:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        while i > 1:
            i //= 2
            self._push_up(i)
        return

    def pre_min(self, ind):
        stack = [(0, self.n - 1, 1)]
        ans = self.initial
        while stack:
            s, t, i = stack.pop()
            if t <= ind:
                ans = min(ans, self.pre[i])
                continue
            m = s + (t - s) // 2
            if ind >= s:
                stack.append((s, m, i << 1))
            if ind >= m + 1:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def post_min(self, ind):
        stack = [(0, self.n - 1, 1)]
        ans = self.initial
        while stack:
            s, t, i = stack.pop()
            if s >= ind:
                ans = min(ans, self.post[i])
                continue
            m = s + (t - s) // 2
            if m >= ind:
                stack.append((s, m, i << 1))
            if t >= ind:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def bisect_left_post_min(self, val):
        s, t, i = 0, self.n - 1, 1
        while s < t:
            m = s + (t - s) // 2
            if self.post[(i << 1) | 1] >= val:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        return t

    def bisect_right_pre_min(self, val):
        s, t, i = 0, self.n - 1, 1
        while s < t:
            m = s + (t - s) // 2
            if self.pre[i << 1] >= val:
                s, t, i = m + 1, t, (i << 1) | 1
            else:
                s, t, i = s, m, i << 1
        return t


class PointSetPreMaxPostMin:

    def __init__(self, n, initial=inf):
        self.n = n
        self.initial = initial
        self.pre = [-initial] * (4 * n)
        self.post = [initial] * (4 * n)
        return

    def _make_tag(self, i, val):
        self.pre[i] = val
        self.post[i] = val
        return

    def _push_up(self, i):
        self.pre[i] = max(self.pre[i << 1], self.pre[(i << 1) | 1])
        self.post[i] = min(self.post[i << 1], self.post[(i << 1) | 1])
        return

    def build(self, nums):

        stack = [(0, self.n - 1, 1)]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self._make_tag(i, nums[s])
                else:
                    stack.append((s, t, ~i))
                    m = s + (t - s) // 2
                    stack.append((s, m, i << 1))
                    stack.append((m + 1, t, (i << 1) | 1))
            else:
                i = ~i
                self._push_up(i)
        return

    def get(self):
        stack = [(0, self.n - 1, 1)]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                val = self.pre[i]
                nums[s] = val
                continue
            m = s + (t - s) // 2
            stack.append((s, m, i << 1))
            stack.append((m + 1, t, (i << 1) | 1))
        return nums

    def point_set(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while True:
            if s == t == ind:
                self._make_tag(i, val)
                break
            m = s + (t - s) // 2
            if ind <= m:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        while i > 1:
            i //= 2
            self._push_up(i)
        return

    def pre_max(self, ind):
        stack = [(0, self.n - 1, 1)]
        ans = -self.initial
        while stack:
            s, t, i = stack.pop()
            if t <= ind:
                ans = max(ans, self.pre[i])
                continue
            m = s + (t - s) // 2
            if ind >= s:
                stack.append((s, m, i << 1))
            if ind >= m + 1:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def post_min(self, ind):
        stack = [(0, self.n - 1, 1)]
        ans = self.initial
        while stack:
            s, t, i = stack.pop()
            if s >= ind:
                ans = min(ans, self.post[i])
                continue
            m = s + (t - s) // 2
            if m >= ind:
                stack.append((s, m, i << 1))
            if t >= ind:
                stack.append((m + 1, t, (i << 1) | 1))
        return ans

    def bisect_left_post_min(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while s < t:
            m = s + (t - s) // 2
            if self.post[(i << 1) | 1] >= val and m >= ind:
                s, t, i = s, m, i << 1
            else:
                s, t, i = m + 1, t, (i << 1) | 1
        return t

    def bisect_right_pre_max(self, ind, val):
        s, t, i = 0, self.n - 1, 1
        while s < t:
            m = s + (t - s) // 2
            if self.pre[i << 1] <= val and m + 1 <= ind:
                s, t, i = m + 1, t, (i << 1) | 1
            else:
                s, t, i = s, m, i << 1
        return t


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):
        """
        url: url of the problem
        tag: algorithm tag
        """

        for _ in range(ac.read_int()):
            n = ac.read_int() + 2
            nums = [-inf] + ac.read_list_ints() + [inf]

            tree = PointSetPreMaxPostMin(n)
            tree.build(nums)

            low = PointSetPreMinPostMin(n)
            low.build([1 if not i or nums[i] >= nums[i - 1] else 0 for i in range(n)])

            def query_rr():
                ind = low.bisect_left_post_min(1)
                v = tree.pre_max(ind)
                r = tree.bisect_left_post_min(ind, v)
                return r

            def query_ll():
                ind = low.bisect_right_pre_min(1)
                v = tree.post_min(ind)
                l = tree.bisect_right_pre_max(ind, v)
                return l

            if low.post[1]:
                ac.lst([-1, -1])
            else:
                ll = query_ll()
                rr = query_rr()
                ac.lst([ll, rr])
            for _ in range(ac.read_int()):
                pos, val = ac.read_list_ints()
                nums[pos] = val
                tree.point_set(pos, val)
                if pos:
                    if nums[pos] >= nums[pos - 1]:
                        low.point_set(pos, 1)
                    else:
                        low.point_set(pos, 0)
                if pos + 1 < n:
                    if nums[pos + 1] >= nums[pos]:
                        low.point_set(pos + 1, 1)
                    else:
                        low.point_set(pos + 1, 0)

                if low.post[1]:
                    ac.lst([-1, -1])
                else:
                    ll = query_ll()
                    rr = query_rr()
                    ac.lst([ll, rr])
        return


Solution().main()
