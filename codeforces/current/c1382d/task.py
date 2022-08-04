import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, p):
    m = 2 * n
    a = []
    best = p[0]
    cnt = 1

    for i in range(1, m):
        if p[i] > best:
            a.append(cnt)
            best = p[i]
            cnt = 1
        else:
            cnt += 1

    if cnt > 0:
        a.append(cnt)

    dp = 1
    for ai in a:
        dp |= dp << ai

    return dp & (1 << n)


def main():
    for _ in range(ri()):
        n = ri()
        p = ria()
        ws('YES' if solve(n, p) else 'NO')


if __name__ == '__main__':
    main()
