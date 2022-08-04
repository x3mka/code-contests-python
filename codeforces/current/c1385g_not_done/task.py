import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a, b):
    cnt = [0] * n
    for i in range(n):
        cnt[a[i] - 1] += 1
        cnt[b[i] - 1] += 1

    for i in range(n):
        if cnt[i] != 2:
            return [-1]

    taken = [-1] * n
    # for i in range(n):
        # if taken[a[i]-1] == -1:
        #     taken[a[i]-1] = i
        # else:
        #     # pair i and taken[a[i]-1]


    idx = [0] * n
    for i in range(n):
        idx[a[i] - 1] = i

    # for x in range(1, n + 1):

    ans = 1
    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        wia(solve(n, a, b))


if __name__ == '__main__':
    main()

