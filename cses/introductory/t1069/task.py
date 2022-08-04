import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    s = rs()
    n = len(s)
    ans = 0
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        ans = max(ans, j - i)
        i = j
    wi(ans)


if __name__ == '__main__':
    main()
