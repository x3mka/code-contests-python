import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, m, a):
    rc = 0
    for i in range(n):
        if sum(a[i]) == 0:
            rc += 1

    cc = 0
    for j in range(m):
        if sum([a[k][j] for k in range(n)]) == 0:
            cc += 1

    return (min(rc, cc) % 2) == 1


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for _ in range(n):
            a.append(ria())
        wi('Ashish' if solve(n, m, a) else 'Vivek')


if __name__ == '__main__':
    main()
