import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, p):
    res = [p[0]]
    d = 1 if p[1] > p[0] else -1

    i = 0
    while i < n - 1:
        j = i + 1
        while j < n and p[i]*d < p[j]*d:
            i = j
            j += 1
        res.append(p[j-1])
        d = -d

    wi(len(res))
    wia(res)


def main():
    for _ in range(ri()):
        n = ri()
        p = ria()
        solve(n, p)


if __name__ == '__main__':
    main()
