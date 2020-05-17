def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def solve(a, b, n, k):
    if k == 0:
        return sum(a)

    a = sorted(a)
    b = sorted(b)
    t = sorted(a[:k] + b[-k:])

    return sum(a[k:] + t[k:])


def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        b = ria()
        print(solve(a, b, n, k))


if __name__ == '__main__':
    main()
