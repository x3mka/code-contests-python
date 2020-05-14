from math import sqrt


def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def f(n):
    if n % 2 == 0:
        return 2
    d = 3
    sqr = int(sqrt(n))
    while d <= sqr and n % d != 0:
        d += 2
    if n % d == 0:
        return d
    return n


def main():
    for _ in range(ri()):
        n, k = ria()
        # first divisor of n + f(n) is always 2
        print(n + f(n) + 2*(k-1))


if __name__ == '__main__':
    main()
