import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter


def main():

    n = ri()
    a = ria()
    c = Counter(a)

    d4 = {k: v for k, v in c.items() if v >= 4}
    d2 = {k: v for k, v in c.items() if 2 <= v < 4}

    q = ri()
    for i in range(q):
        op, x = rs().split()
        x = int(x)
        if x not in c:
            c[x] = 0
        if op == "+":
            c[x] += 1
        else:
            c[x] -= 1

        if c[x] >= 4:
            d4[x] = c[x]
            if x in d2:
                del d2[x]

        if c[x] >= 2 and c[x] < 4:
            d2[x] = c[x]

        if c[x] < 4 and x in d4:
            del d4[x]
            d2[x] = c[x]
        if c[x] < 2 and x in d2:
            del d2[x]

        first_key = lambda d: next(iter(d))

        if len(d4) > 1 or \
            len(d4) == 1 and len(d2) > 1 or \
            len(d4) == 1 and d4[first_key(d4)] >= 8 or \
            len(d4) == 1 and d4[first_key(d4)] >= 6 and len(d2) > 0:
            ws('YES')
        else:
            ws('NO')


if __name__ == '__main__':
    main()
