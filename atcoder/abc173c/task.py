import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


import itertools

def powerset(iterable, low=0, high=None):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)+1
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(low, high))


def solve(h, w, k, a):
    ans = 0
    rows = [i for i in range(h)]
    cols = [j for j in range(w)]

    for rr in powerset(rows):
        for cc in powerset(cols):
            rrs = set(rr)
            ccs = set(cc)
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if i not in rrs and j not in ccs and a[i][j] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1

    return ans


def main():
    h, w, k = ria()
    a = []
    for _ in range(h):
        a.append(rs())
    wi(solve(h, w, k, a))


if __name__ == '__main__':
    main()
