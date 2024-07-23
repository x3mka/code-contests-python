import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    comp = [{i} for i in range(n)]

    ws('YES')
    ans = []

    for x in range(n-1, 0, -1):
        rem = {}
        for c in comp:
            i = next(iter(c))
            r = a[i] % x
            if r not in rem:
                rem[r] = []
            rem[r].append((i, c))
            if len(rem[r]) == 2:
                ans.append([rem[r][0][0]+1, rem[r][1][0]+1])
                rem[r][0][1].update(rem[r][1][1])
                comp.remove(rem[r][1][1])
                break

    for b in reversed(ans):
        wia(b)

def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
