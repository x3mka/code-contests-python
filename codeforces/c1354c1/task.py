def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


from math import pi, sin, tan


def solve(n):
    if n % 2 == 0:
        return 1.0 / tan(pi / (2*n))
    else:
        return 1.0 / sin(pi / (2*n))


def main():
    for _ in range(ri()):
        n = ri()
        print(solve(n))


if __name__ == '__main__':
    main()
