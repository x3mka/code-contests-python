def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, x, a):
    odds_count = sum(1 for i in a if i % 2 == 1)
    even_count = n - odds_count

    for i in range(1, x+1, 2):  # take i odd and x-i even
        if odds_count >= i and even_count >= x-i:
            return True

    return False


def main():
    for _ in range(ri()):
        n, x = ria()
        a = ria()
        print('Yes' if solve(n, x, a) else 'No')


if __name__ == '__main__':
    main()
