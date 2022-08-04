import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(s):
    n = len(s)
    turn = 1
    while True:
        if n <= 1:
            return turn == -1

        i = 0
        while i < n-1:
            if s[i] == '0' and s[i+1] == '1' or s[i] == '1' and s[i+1] == '0':
                break
            i += 1
        if i == n-1:
            return turn == -1

        s = s[:i] + s[i+2:]
        n = len(s)
        turn = -turn


def main():
    for _ in range(ri()):
        s = rs()
        wi('DA' if solve(s) else 'NET')


if __name__ == '__main__':
    main()
