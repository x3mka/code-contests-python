def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


import itertools

def solve(d):
    ans = 0
    n = len(d)
    indices = list(range(n))

    for r in range(1, n+1):
        d = sorted(d, reverse=True)
        for c in itertools.combinations(indices, r):
            ok = True
            for i in range(len(c)):
                if d[c[i]] == 0:
                    ok = False
                    break
            if ok:
                ans += 1
                for i in range(len(c)):
                    d[c[i]] -= 1

    return ans


def main():
    for _ in range(ri()):
        a, b, c = ria()
        print(solve([a, b, c]))


if __name__ == '__main__':
    main()
