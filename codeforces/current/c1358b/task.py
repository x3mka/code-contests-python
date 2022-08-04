def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, a):
    a = sorted(a)
    i = n-1
    while i >= 0 and a[i] > i+1:
        i -= 1
    return i + 2


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        print(solve(n, a))


if __name__ == '__main__':
    main()
