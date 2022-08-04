def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, m, x, y, a):
    c2 = min(y, 2*x)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                k = j
                while k < m and a[i][k] == 0:
                    a[i][k] = 1
                    k += 1
                r = k - j
                cnt += c2 * (r // 2) + x * (r % 2)
                j = k


    return cnt


def main():
    for _ in range(ri()):
        n, m, x, y = ria()
        a = []
        for __ in range(n):
            a.append([1 if x == '*' else 0 for x in rs()])
        print(solve(n, m, x, y, a))


if __name__ == '__main__':
    main()
