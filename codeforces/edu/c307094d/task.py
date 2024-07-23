import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    for i in range(4):
        a[i].sort()
    best = [a[i][0] for i in range(4)]
    ans = max(best) - min(best)

    merged = [0] * sum(n)

    idx = [0] * 4
    d = [-1] * 4
    while True:
        c_idx = [i for i in range(4) if idx[i] < n[i]]
        c_vals = [a[i][idx[i]] for i in c_idx]
        mn = min(c_vals)
        min_indices = [i for i in range(len(c_idx)) if c_vals[i] == mn]
        min_i = min_indices[0]
        d[c_idx[min_i]] = mn
        merged[sum(idx)] = mn
        idx[c_idx[min_i]] += 1

        if all([d[i] > -1 for i in range(4)]):
            v = max(d) - min(d)
            if v < ans:
                ans = v
                best = d.copy()

        if all([idx[i] == n[i] for i in range(4)]):
            break

    return best


def main():
    n = [0] * 4
    a = [[0] for i in range(4)]
    for i in range(4):
        n[i] = ri()
        a[i] = ria()

    wia(solve(n, a))


if __name__ == '__main__':
    main()