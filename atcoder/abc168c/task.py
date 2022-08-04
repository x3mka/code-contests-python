def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


import math


def solve(a, b, h, m):
    h_a = 90 - 360 / 12 * (m / 60 + h)
    m_a = 90 - 360 / 60 * m
    angle = m_a - h_a

    return (a*a + b*b - 2*a*b*math.cos(angle*math.pi/180))**0.5



def main():
    a, b, h, m= ria()
    print(solve(a, b, h, m))


if __name__ == '__main__':
    main()
