import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')



def main():
    n, m = ria()
    a = ria()
    b = ria()

    t = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            t[i][j] = a[i] & b[j]

    for ans in range(0, 513):
        ok = True
        for i in range(n):
            j_exists = False
            for j in range(m):
                if t[i][j] | ans == ans:
                    j_exists = True
                    break
            if not j_exists:
                ok = False
                break
        if ok:
            wi(ans)
            return


if __name__ == '__main__':
    main()
