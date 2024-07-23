import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(s1, s2):
    return " ".join([s2[0] + s1[1:], s1[0] + s2[1:]])


def main():
    for _ in range(ri()):
        s1, s2 = rs().split()
        ws(solve(s1, s2))


if __name__ == '__main__':
    main()
