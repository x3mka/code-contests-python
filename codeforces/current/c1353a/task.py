def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def solve(n, m):
    if n == 1:
        return 0
    if n == 2:
        return m
    return 2*m


def main():
    for _ in range(ri()):
        n, m = ria()
        print(solve(n, m))


if __name__ == '__main__':
    main()
