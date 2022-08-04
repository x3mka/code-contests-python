import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(s):
    n = len(s)
    g = []
    i = 0
    while i < n:
        if s[i] == '0':
            i += 1
        else:
            j = i
            while j < n and s[j] == '1':
                j += 1
            g.append(j - i)
            i = j + 1
    g.sort(reverse=True)
    return sum(g[::2])


def main():
    for _ in range(ri()):
        s = rs()
        wi(solve(s))


if __name__ == '__main__':
    main()
