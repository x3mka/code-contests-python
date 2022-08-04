def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(x, h, m):
    cnt = 0
    while True:
        if '7' in (str(h) + str(m)):
            break
        if x <= m:
            m -= x
        else:
            m = m - x + 60
            h -= 1
            if h == -1:
                h = 23
        cnt += 1

    return cnt


def main():
    x = ri()
    h, m = ria()
    print(solve(x, h, m))


if __name__ == '__main__':
    main()
