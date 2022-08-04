def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, k):
    if n % 2 != k % 2:
        return False

    if n < k*k:
        return False

    return True



def main():
    for _ in range(ri()):
        n, k = ria()
        print('YES' if solve(n, k) else 'NO')


if __name__ == '__main__':
    main()
