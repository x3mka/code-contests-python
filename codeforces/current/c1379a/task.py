import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, s):
    t = 'abacaba'
    m = len(t)

    for i in range(n - m + 1):
        if s[i] != '?' and s[i] != t[0]:
            continue
        ss = [si for si in s]
        ok = True
        for j in range(m):
            if ss[i + j] != '?' and s[i + j] != t[j]:
                ok = False
                break
            ss[i + j] = t[j]
        for j in range(n):
            if ss[j] == '?':
                ss[j] = 'z'
        cnt = 0
        for ii in range(n - m + 1):
            f = True
            for j in range(m):
                if ss[ii + j] != t[j]:
                    f = False
                    break
            if f:
                cnt += 1

        if ok and cnt == 1:
            ws('Yes')
            ws(''.join(ss))
            return

    ws('No')


def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        solve(n, s)


if __name__ == '__main__':
    main()
