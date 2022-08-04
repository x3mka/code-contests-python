def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n, a):
    ok = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if not (i == n-1 or i < n-1 and a[i+1][j] == 1 or j == n-1 or j < n-1 and a[i][j+1] == 1):
                    ok = False
                    break
    return ok


def main():
    for _ in range(ri()):
        n = ri()
        a = []
        for __ in range(n):
            a.append([int(x) for x in rs()])
        print('YES' if solve(n, a) else 'NO')


if __name__ == '__main__':
    main()
