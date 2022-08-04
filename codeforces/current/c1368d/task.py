import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def score(a):
    return sum([ai*ai for ai in a])

def solve(n, a):
    bn = 22
    cnt = [0] * bn
    for i in range(n):
        for j in range(bn):
            if a[i] & (1 << j):
                cnt[j] += 1

    b = [0] * n
    for i in range(n):
        for j in range(bn):
            if cnt[j] > 0:
                b[i] += (1 << j)
                cnt[j] -= 1

    return score(b)


def main():
    n = ri()
    a = ria()
    wi(solve(n, a))


if __name__ == '__main__':
    main()
