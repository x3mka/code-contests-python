def ri(): return int(input())
def ria(): return list(map(int, input().split()))


def solve(n, k, a):
    flag = False

    for i in range(n):
        if a[i] < k:
            a[i] = 0
        elif a[i] > k:
            a[i] = 2
        else:
            a[i] = 1

        if a[i] == 1:
            flag = True

    if not flag:
        return False
    if n == 1:
        return True

    for i in range(n):
        for j in range(i+1, i+3):
            if j < n and a[i] and a[j]:
                return True

    return False


def main():
    for _ in range(ri()):
        n, k = ria()
        a = ria()
        print('yes' if solve(n, k, a) else 'no')


if __name__ == '__main__':
    main()
