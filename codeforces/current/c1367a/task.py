import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(b):
    n = len(b)
    a = [b[0]]
    for i in range(1, n // 2):
        a.append(b[i*2])
    a.append(b[n-1])
    return ''.join(a)


def main():
    for _ in range(ri()):
        b = rs()
        ws(solve(b))


if __name__ == '__main__':
    main()
