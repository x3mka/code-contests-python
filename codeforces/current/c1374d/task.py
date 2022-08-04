import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, a):
    b = [k - a[i] % k if a[i] % k > 0 else 0 for i in range(n)]
    if sum([1 for bi in b if bi == 0]) == n:
        return 0

    b = sorted(b)

    for i in range(n):
        if b[i] == 0:
            continue
        j = i + 1
        while j < n and b[j] == b[i]:
            b[j] += k * (j-i)
            j += 1

    b = sorted(b)

    return b[n-1] + 1



def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        wi(solve(n, k, a))


if __name__ == '__main__':
    main()
