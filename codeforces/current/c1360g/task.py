def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n, m, a, b):
    if a * n != b * m:
        print('NO')
        return

    d = 1
    while d < m:
        if d * n % m == 0:
            break
        d += 1

    s = [[0]*m for _ in range(n)]
    for j in range(a):
        s[0][j] = 1
    for i in range(1, n):
        for j in range(a):
            s[i][(j+d*i)%m] = 1

    print('YES')
    for i in range(n):
        print(''.join([str(x) for x in s[i]]))
    return


def main():
    for _ in range(ri()):
        n, m, a, b = ria()
        solve(n, m, a, b)


if __name__ == '__main__':
    main()
