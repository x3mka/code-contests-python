import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, s):
    i = 0
    while i < len(s)-1:
        if s[i] == '(' and s[i+1] == ')':
            s = s[:i] + s[i+2:]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1

    return len(s) // 2


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        wi(solve(n, s))


if __name__ == '__main__':
    main()
