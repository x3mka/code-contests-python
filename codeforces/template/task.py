def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, k):
    return 0


def main():
    for _ in range(ri()):
        n, k = ria()
        print(solve(n, k))


if __name__ == '__main__':
    main()
