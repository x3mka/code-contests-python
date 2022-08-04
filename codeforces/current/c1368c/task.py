import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def print_sq(si, sj, skip_first=False):
    if not skip_first:
        wia([si, sj])
    wia([si, sj + 1])
    wia([si, sj + 2])
    wia([si + 1, sj + 2])
    wia([si + 2, sj + 2])
    wia([si + 2, sj + 1])
    wia([si + 2, sj])
    wia([si + 1, sj])

def solve(n):
    k = 8 * (n+1) - n
    wi(k)
    for i in range(n+1):
        print_sq(2*i, 2*i, i>0)


def main():
    n = ri()
    solve(n)


if __name__ == '__main__':
    main()
