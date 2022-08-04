import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a, b):
    d = {}
    for i in range(n):
        c = a[i]
        if c not in d:
            d[c] = set()
        d[c].add(i)

    bb = sorted([(b[i], i) for i in range(n)])

    ans = 0
    for idx in range(n):
        bi, i = bb[idx]

        for ai, v in d.items():
            if i in v:
                break
        # v.remove(i)
        if ai == bi:
            continue
        if ai > b[i]:
            return -1

        ii = [vi for vi in v if b[vi] >= bi]
        for iii in ii:
            v.remove(iii)

        if bi not in d:
            d[bi] = set()
        d[bi].update(ii)
        if len(v) == 0:
            del d[ai]
        ans += 1

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = rs()
        b = rs()
        wi(solve(n, a, b))


if __name__ == '__main__':
    main()
