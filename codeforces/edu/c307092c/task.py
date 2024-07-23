import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, a, b):
    ans = 0
    i, j = 0, 0
    while j < m:
        while i < n and a[i] < b[j]:
            i += 1

        if i < n and a[i] == b[j]:
            new_i = i
            while new_i < n and a[new_i] == a[i]:
                new_i += 1
            new_j = j
            while new_j < m and b[new_j] == b[j]:
                new_j += 1
            ans += (new_i - i) * (new_j - j)
            i = new_i
            j = new_j
        else:
            j += 1

    return ans


def main():
    n, m = ria()
    a = ria()
    b = ria()
    wi(solve(n, m, a, b))


if __name__ == '__main__':
    main()