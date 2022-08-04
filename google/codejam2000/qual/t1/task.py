import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    trace = sum([a[i][i] for i in range(n)])
    rr = sum(1 for i in range(n) if len(set(a[i])) != n)
    cc = sum([1 for i in range(n) if len(set([a[j][i] for j in range(n)])) != n])
    return ' '.join([str(trace), str(rr), str(cc)])


def main():
    for t in range(ri()):
        n = ri()
        a = []
        for _ in range(n):
            a.append(ria())
        ws("Case #{}: {}".format(t+1, solve(n, a)))


if __name__ == '__main__':
    main()
