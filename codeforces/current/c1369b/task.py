import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, s):
    if s.count('1') == 0 or s.count('0') == 0:
        return s

    ss = s[:s.index('1')]
    i = 0
    while i < n and s[n-i-1] == '1':
        i += 1
    se = s[-i:] if i > 0 else ""

    c = ""
    if len(ss) + len(se) < n:
        c = "0"

    return ss + c + se


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        ws(solve(n, s))


if __name__ == '__main__':
    main()
