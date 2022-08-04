import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s, c):
    if n == 1:
        return 0 if s[0] == c else 1

    mid = n // 2
    c1 = s[:mid].count(c)
    c2 = s[mid:].count(c)

    return min(mid - c1 + solve(mid, s[mid:], chr(ord(c) + 1)), mid - c2 + solve(mid, s[:mid], chr(ord(c) + 1)))


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        wi(solve(n, s, 'a'))


if __name__ == '__main__':
    main()
