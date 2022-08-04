import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    i = 0
    while i < n - 1 and a[i] > a[i+1]:
        i += 1
    k = n-1
    while k > 1 and a[k] > a[k-1]:
        k -= 1
    if k > i + 1:
        for j in range(i+1, k):
            if a[j] > a[i] and a[j] > a[k]:
                break
        ws('YES')
        wia([i + 1, j + 1, k + 1])
    else:
        ws('NO')


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
