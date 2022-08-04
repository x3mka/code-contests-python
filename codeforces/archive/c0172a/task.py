def rs(): return input().strip()


def ri(): return int(input())


def ria(): return list(map(int, input().split()))


def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, s):
    i = 0
    m = len(s[0])
    while i < m:
        ok = True
        c = s[0][i]
        for j in range(1, n):
            if s[j][i] != c:
                ok = False
                break
        if ok:
            i += 1
        else:
            return i

    return i-1


def main():
    n = ri()
    s = []
    for _ in range(n):
        s.append(rs())
    print(solve(n, s))


if __name__ == '__main__':
    main()