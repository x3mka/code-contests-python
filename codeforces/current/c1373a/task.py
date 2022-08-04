import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')




def solve(a, b, c):
    if a < c:
        r1 = 1
    else:
        r1 = -1

    if c < a * b:
        r2 = b
    else:
        r2 = -1

    return [r1, r2]


def main():
    for _ in range(ri()):
        a, b, c = ria()
        wia(solve(a, b, c))


if __name__ == '__main__':
    main()
