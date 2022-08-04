import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(s, m, b):
    n = len(s)

    # bi = sorted([(b[i], i) for i in range(m)])
    ss = sorted([si for si in s], reverse=True)

    t = [''] * m
    ci = 0
    not_taken = [i for i in range(m)]

    for _ in range(m):
        cnt = 0
        tt = set()
        for j in range(m):
            if t[j] == '' and b[j] == 0:
                tt.add(j)
                not_taken.remove(j)
                cnt += 1
        if cnt == 0:
            break

        while True:
            k = 0
            while k < cnt and ci+k < n and ss[ci+k] == ss[ci]:
                k += 1
            if k == cnt:
                break
            else:
                ci += k

        for j in tt:
            t[j] = ss[ci]

        k = 0
        while ci + k < n and ss[ci+k] == ss[ci]:
            k += 1
        ci += k

        for j in not_taken:
            for k in tt:
                b[j] -= abs(j - k)

    return ''.join(t)


def main():
    for _ in range(ri()):
        s = rs()
        m = ri()
        b = ria()
        ws(solve(s, m, b))


if __name__ == '__main__':
    main()
