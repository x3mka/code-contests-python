import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n):
    return (n + 1) // 2


def main():
    for _ in range(ri()):
        n = ri()
        wi(solve(n))


if __name__ == '__main__':
    main()
