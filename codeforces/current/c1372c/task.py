import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')



def s1(n, a):
    cnt = 0
    c1 = set()
    c2 = set()
    bad = 0
    for i in range(n):
        if a[i] == i + 1:
            if c1 == c2:
                if len(c1) > 0:
                    cnt += 1 + bad
                    bad = 0
                    c1 = set()
                    c2 = set()
            else:
                bad = 1
        else:
            c1.add(i + 1)
            c2.add(a[i])
    if len(c1) > 0:
        cnt += 1 + bad
    return cnt


def solve(n, a):
    cnt = 0
    c = 0
    for i in range(n):
        if a[i] == i + 1:
            if c > 0:
                cnt += 1
                c = 0
        else:
            c += 1
    if c > 0:
        cnt += 1
    return min(cnt, 2)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
