import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import heapq

def solve(n, a):
    a = sorted(a, reverse=True)
    ans = 0

    h = [-a[0]]
    heapq.heapify(h)

    for i in range(1, n):
        p = heapq.heappop(h)
        ans += -p
        heapq.heappush(h, -a[i])
        heapq.heappush(h, -a[i])

    return ans


def main():
    n = ri()
    a = ria()
    wi(solve(n, a))


if __name__ == '__main__':
    main()
