import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def get_b(a):
    b = []
    d = {}
    mx_so_far = 0
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
        if d[a[i]] >= 2 and a[i] > mx_so_far:
            mx_so_far = a[i]
        if mx_so_far > 0:
            b.append(mx_so_far)
    return b

def solve(n, a):
    s = sum(a)

    b = get_b(a)
    s += sum(b)

    b = get_b(b)

    n = len(b)
    for i in range(n):
        s += (n-i) * b[i]
    return s


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
