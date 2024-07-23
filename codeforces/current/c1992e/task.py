import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


M = 3000


def solve(n):
    s = str(n)
    L = len(s)
    sols = []

    for l in range(1, 7):   # iterate over length of result n * a - b done as strings
        ds = ""
        for i in range(l):
            ds += s[i % L]

        res = int(ds)  # n * a - b = res
        for a in range(1, 10001):
            b = n * a - res
            if 1 <= b <= 10000 and L * a - b == l:
                sols.append([a, b])

    wi(len(sols))
    for sol in sols:
        wia(sol)


def main():
    for _ in range(ri()):
        n = ri()
        solve(n)


if __name__ == '__main__':
    main()
