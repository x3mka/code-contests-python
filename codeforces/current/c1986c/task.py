import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, s, ind, c):
    sa = list(s)
    sc = sorted(list(c))
    s_ind = sorted(ind)

    l = 0
    r = m-1

    for i in range(m):
        if i < m-1 and s_ind[i] == s_ind[i+1]:
            sa[s_ind[i]-1] = sc[r]
            r -= 1
        else:
            sa[s_ind[i]-1] = sc[l]
            l += 1

    return ''.join(sa)


def main():
    for _ in range(ri()):
        n, m = ria()
        s = rs()
        ind = ria()
        c = rs()
        ws(solve(n, m, s, ind, c))


if __name__ == '__main__':
    main()
