def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(w):
    return w % 2 == 0 and w // 2 >= 2


def main():
    w = ri()
    print('YES' if solve(w) else 'NO')


if __name__ == '__main__':
    main()
