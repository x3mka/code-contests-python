import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from itertools import permutations


def main():
    s = rs()
    n = len(s)

    ans = 0
    st = set()
    for p in permutations(s):
        t = ''.join(p)
        if t not in st:
            ans += 1
        st.update([t])
    wi(len(st))
    for t in sorted(st):
        ws(t)


if __name__ == '__main__':
    main()
