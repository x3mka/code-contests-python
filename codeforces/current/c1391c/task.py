import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from itertools import permutations
from collections import deque


def has_cycle(n, g):
    for start in range(n):
        prev = [-1] * n
        t = [-1] * n

        q = deque()
        q.append(start)
        t[start] = 0

        while q:
            v = q.popleft()

            for w in g[v]:
                if t[w] != -1:
                    if t[w] >= t[v]:
                        return True
                else:
                    t[w] = t[v] + 1
                    prev[w] = v
                    q.append(w)
    return False


def test(n, a):
    g = [[] for _ in range(n)]
    for i in range(n):
        j = i - 1
        while j >= 0 and a[j] < a[i]:
            j -= 1
        if j >= 0:
            g[i].append(j)
            g[j].append(i)
        j = i + 1
        while j < n and a[j] < a[i]:
            j += 1
        if j < n:
            g[i].append(j)
            g[j].append(i)
    return has_cycle(n, g)


def main():
    m = 1000000007
    n = ri()

    ans = 1

    for i in range(1, n + 1):
        ans = (ans * i) % m

    p2 = 1
    for i in range(n-1):
        p2 = (p2 * 2) % m

    ans = (ans - p2) % m

    wi(ans)
    return


    # for n in range(3, 10):
    #     a = [i + 1 for i in range(n)]
    #
    #     cnt = 0
    #     for p in permutations(a):
    #         if test(n, p):
    #             cnt += 1
    #
    #     wia([n, cnt])


if __name__ == '__main__':
    main()
