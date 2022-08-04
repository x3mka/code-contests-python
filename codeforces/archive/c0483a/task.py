def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(l, r):
    if r - l < 2:
        return [-1]
    if r - l == 2:
        if l % 2 == 0:
            return [l, l+1, l+2]
        else:
            return [-1]

    if l % 2 == 1:
        l += 1
    return [l, l + 1, l + 2]


def main():
    l, r = ria()
    print(ia_to_s(solve(l, r)))


if __name__ == '__main__':
    main()
