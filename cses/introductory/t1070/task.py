import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()

    if n == 1:
        wi(1)
        return
    if n == 2 or n == 3:
        ws('NO SOLUTION')
        return

    s = [i+1 for i in range(n)]
    p = list(reversed(s[::2])) + list(reversed(s[1::2]))
    wia(p)


if __name__ == '__main__':
    main()
