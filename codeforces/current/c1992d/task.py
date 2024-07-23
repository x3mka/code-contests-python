import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, m, k, a):
    a = 'L' + a + 'L'
    n += 2
    i = 0
    while i < n:
        if a[i] == 'C':
            return 'NO'
        if a[i] == 'W':
            k -= 1
            if k < 0:
                return "NO"
            i += 1
        if a[i] == 'L':
            next_log = -1
            next_water = -1
            for j in range(1, m+1):
                if i+j < n:
                    if a[i+j] == 'L':
                        next_log = i + j
                    if a[i+j] == 'W':
                        next_water = i + j
            # if possible we jump on a log, otherwise in water
            if next_log > -1:
                i = next_log
            elif next_water > -1:
                i = next_water
            else:
                i += 1

    return "YES"


def main():
    for _ in range(ri()):
        n, m, k = ria()
        a = rs()
        ws(solve(n, m, k, a))


if __name__ == '__main__':
    main()
