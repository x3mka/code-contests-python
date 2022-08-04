import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from functools import lru_cache


def solve(x):
    if x <= 0:
        return 0

    default_state = 0

    def predicate(s):
        return s == 1

    def new_state(state, pos, d):
        return state + d * (1 if pos % 2 == 1 else -1)

    @lru_cache(maxsize=None)
    def go(pos, restricted, state):
        """
        :param pos: index value from right in the given integer
        :param restricted: if restricted, digit span is [0,9], otherwise [0,digits[pos]]
        :param state: supporting state
        :return:
        """
        if pos == -1:
            # matching condition
            return 1 if predicate(state) else 0

        ans = 0
        up = a[pos] if restricted else 9
        for d in range(up + 1):
            ans += go(pos - 1, restricted and d == a[pos], new_state(state, pos, d))
        return ans

    # digits array in reverse order
    a = []
    while x > 0:
        a.append(x % 10)
        x //= 10

    n = len(a)
    return go(n-1, True, default_state)


def solve_in_range(a, b):
    return solve(b) - solve(a-1)


def main():
    for _ in range(ri()):
        a, b = ria()
        wi(solve_in_range(a, b))


if __name__ == '__main__':
    main()
