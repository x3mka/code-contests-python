import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, a):
    odds = [i for i in range(2*n) if a[i] % 2 == 1]
    evens = [i for i in range(2 * n) if a[i] % 2 == 0]

    n_odds = len(odds)
    n_even = len(evens)

    # all even
    if n_odds == 0:
        for i in range(n-1):
            wia([evens[2*i]+1, evens[2*i+1]+1])
        return

    # there are odds
    if n_odds % 2 == 0:
        odds.pop()
        odds.pop()
    else:
        odds.pop()
        evens.pop()

    k = 0
    while k < n-1 and 2*k+1 < len(odds):
        wia([odds[2 * k] + 1, odds[2 * k + 1] + 1])
        k += 1

    i = 0
    while k < n-1:
        wia([evens[2 * i] + 1, evens[2 * i + 1] + 1])
        k += 1
        i += 1


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


if __name__ == '__main__':
    main()
