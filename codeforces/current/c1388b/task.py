import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    k = (n + 3) // 4
    return '9' * (n - k) + '8' * k

    # eights = 1 + (n // 4)
    # return '9' * (n - eights) + '8' * eights

    best_r = 0
    best_x = ''
    for eights in range(1, n + 1):
        x = '9' * (n - eights) + '8' * eights
        k = ''.join([format(int(si), 'b') for si in x])
        if len(k) <= n:
            continue
        r = int(k[:-n], 2)
        if r > best_r:
            best_r = r
            best_x = x

    return best_x


def main():
    for _ in range(ri()):
        n = ri()
        ws(solve(n))


if __name__ == '__main__':
    main()
