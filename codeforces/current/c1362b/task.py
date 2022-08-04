import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')



def solve(n, s):
    ss = set(s)
    for x in range(1, 1025):
        pp = set([si ^ x for si in s])
        if ss == pp:
            return x
    return -1


def main():
    for _ in range(ri()):
        n = ri()
        s = ria()
        print(solve(n, s))


if __name__ == '__main__':
    main()
