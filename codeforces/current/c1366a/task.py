import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(a, b):
   return min((a+b)//3, a, b)


def main():
    for _ in range(ri()):
        a, b = ria()
        wi(solve(a, b))


if __name__ == '__main__':
    main()
