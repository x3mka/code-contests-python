def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(b, k, a):
    n = 0
    for i in range(k):
        n = (b * n + a[i]) % 2
    return n


def main():
        b, k = ria()
        a = ria()
        print('even' if solve(b, k, a) % 2 == 0 else 'odd')


if __name__ == '__main__':
    main()
