import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(h, n, a, c):
    # can be simulated with a heap
    # x = []
    # for i in range(n):
    #     x.append((1, i))
    # heapq.heapify(x)
    # turn = 1
    # while h > 0:
    #     t, i = heapq.heappop(x)
    #     h -= a[i]
    #     turn = t
    #     heapq.heappush(x, (t + c[i], i))
    # return turn

    # bisect result, invariant:   lo (cannot kill), hi (can kill)
    lo = 0
    hi = max(c) * ((h // sum(a)) + 1)
    while hi - lo > 1:
        mid = (hi + lo) // 2

        hp = 0
        for i in range(n):
            hp += ((mid-1) // c[i]) * a[i] + a[i]
        can_kill = hp >= h
        if can_kill:
            hi = mid
        else:
            lo = mid
    return hi

def main():
    for _ in range(ri()):
        h, n = ria()
        a = ria()
        c = ria()
        wi(solve(h, n, a, c))


if __name__ == '__main__':
    main()
