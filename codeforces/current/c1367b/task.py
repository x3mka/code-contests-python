import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    cnt01 = sum([1 for i in range(n) if a[i] % 2 == 0 and i % 2 == 1])
    cnt10 = sum([1 for i in range(n) if a[i] % 2 == 1 and i % 2 == 0])
    return cnt01 if cnt01 == cnt10 else -1


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
