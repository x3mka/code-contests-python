def rs(): return input().strip()


def ri(): return int(input())


def ria(): return list(map(int, input().split()))


def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(s):
    if len(s) <= 10:
        return s
    return ''.join([s[0], str(len(s) - 2), s[-1]])


def main():
    n = ri()
    for _ in range(n):
        print(solve(rs()))


if __name__ == '__main__':
    main()