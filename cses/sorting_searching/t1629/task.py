import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    s = []
    for i in range(n):
        s.append(ria())

    s = sorted(s, key=lambda x: (x[1], x[0]))

    ans = 1
    last = s[0][1]

    for i in range(1, n):
        if s[i][0] >= last:
            ans += 1
            last = s[i][1]

    wi(ans)


if __name__ == '__main__':
    main()
