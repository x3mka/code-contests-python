import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    s = int(n ** 0.5) + 1
    prime = True
    best = n

    for i in range(2, s):
        if n % i == 0:
            prime = False
            d = n // i
            best = min(best, min(max(i * (d - 1), i), max(d * (i - 1), d)))

    if prime:
        return [1, n-1]

    return [best, n-best]


def main():
    for _ in range(ri()):
        n = ri()
        wia(solve(n))


if __name__ == '__main__':
    main()
