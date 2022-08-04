import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    m = max(a) + 1
    s = 'a' * m
    ws(s)
    for i in range(n):
        t = [si for si in s]
        if t[a[i]] == 'a':
            t[a[i]] = 'b'
        else:
            t[a[i]] = 'a'

        s = ''.join(t)
        ws(s)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
