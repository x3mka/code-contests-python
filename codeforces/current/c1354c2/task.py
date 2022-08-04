def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


from math import pi, sin, cos


def solve(n):
    return cos(pi / (4*n)) / sin(pi / (2*n))


def main():
    for _ in range(ri()):
        n = ri()
        print(solve(n))


if __name__ == '__main__':
    main()
