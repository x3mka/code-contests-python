import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, k, l, d):
    p = [i for i in range(k + 1)]
    p += p[1:k][::-1]

    for t in range(2 * k):
        wia([d[i] + p[t % (2 * k)] for i in range(n)])

    ws(' ')
    return

    for st in range(2 * k):
        ok = True
        s = -1
        t = 0
        while s < n - 1:
            if d[s + 1] + p[(st + t + 1) % (2 * k)] <= l:
                s += 1
            t += 1
            if s >= 0 and d[s] + p[(st + t) % (2 * k)] > l:
                ok = False
                break

        if ok:
            return True

    return False


def main():
    for _ in range(ri()):
        n, k, l = ria()
        d = ria()
        ws('Yes' if solve(n, k, l, d) else 'No')


if __name__ == '__main__':
    main()
