import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from functools import lru_cache


def solve(x):
    # handle edge cases
    if x < 0:
        return 0

    default_state = 1

    def predicate(s):
        return s == 10

    def new_state(state, pos, d):
        return state * d

    def early_stop(s):
        return s == 0

    @lru_cache(maxsize=None)
    def go(pos, restricted, state):
        """
        :param pos: index value from right in the given integer
        :param restricted: if restricted, digit span is [0,9], otherwise [0,digits[pos]]
        :param state: supporting state
        :return:
        """
        if early_stop(state):
            return 0

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
    a, b = ria()
    wi(solve_in_range(a, b))


if __name__ == '__main__':
    main()
