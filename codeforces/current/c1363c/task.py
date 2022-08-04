def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


from collections import deque


def solve(n, x, ee):
    if n == 1:
        return 'Ayush'

    dx = 0
    for e in ee:
        if e[0] == x or e[1] == x:
            dx += 1

    if dx == 1:
        return 'Ayush'

    return 'Ashish' if (n-1) % 2 == 0 else 'Ayush'


def main():
    for _ in range(ri()):
        n, x = ria()
        ee = []
        for __ in range(n-1):
            ee.append(ria())
        print(solve(n, x, ee))


if __name__ == '__main__':
    main()
