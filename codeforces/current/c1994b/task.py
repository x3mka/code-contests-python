import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, t):
    x = 1
    ones = sum([1 for i in range(n) if s[i] == '1'])

    for i in range(n-1, -1, -1):
        if s[i] == '1':
            ones -= 1
        if s[i] == t[i]:
            continue
        if ones > 0:
            continue
        if s[i] == '0':
            return 'NO'

    return "YES"

def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        t = rs()
        wi(solve(n, s, t))


if __name__ == '__main__':
    main()
