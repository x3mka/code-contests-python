import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def good(a):
    n = len(a)
    i = 0
    j = n-1
    b = []
    while i <= j:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j -= 1

    for i in range(n-1):
        if b[i] > b[i + 1]:
            return False
    return True


def solve(n, a):
    lo = -1
    hi = n-1
    while hi > lo + 1:
        mid = (lo + hi) // 2
        if good(a[mid:]):
            hi = mid
        else:
            lo = mid
    return hi


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
