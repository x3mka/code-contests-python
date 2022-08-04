import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, m, a):
    k = (n+m-1)//2
    ones = [0]*k
    zeros = [0]*k

    for i in range(n):
        for j in range(m):
            if (n+m) % 2 == 0 and i+j == k:  # not counting diagonal
                continue
            kk = i + j
            if kk >= k:
                kk = n - i - 1 + m - j - 1

            if a[i][j] == 0:
                zeros[kk] += 1
            else:
                ones[kk] += 1

    return sum([min(zeros[i], ones[i]) for i in range(k)])


def main():
    for _ in range(ri()):
        n, m = ria()
        a = []
        for _ in range(n):
            a.append(ria())
        wi(solve(n, m, a))


if __name__ == '__main__':
    main()
