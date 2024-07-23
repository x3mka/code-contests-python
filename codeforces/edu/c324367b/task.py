import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def main():
    n = ri()
    a = ria()

    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = a[i-1] ^ b[i-1]

    q = ri()
    for i in range(q):
        l, r = ria()
        wi(b[r] ^ b[l-1])


if __name__ == '__main__':
    main()
