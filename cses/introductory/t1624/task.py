import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = 8
    b = []
    for _ in range(n):
        b.append(rs())

    def go(start):
        if start == n:
            return 1
        res = 0
        for i in range(n):
            if b[i][start] == '*':
                continue
            ok = True
            for j in range(len(pos)):
                if i == pos[j] or abs(start - j) == abs(i - pos[j]):
                    ok = False
                    break
            if ok:
                pos.append(i)
                res += go(start + 1)
                pos.pop()
        return res

    pos = []
    wi(go(0))


if __name__ == '__main__':
    main()
