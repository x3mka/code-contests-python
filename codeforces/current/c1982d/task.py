import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ria2(): return list(map(int, list(sys.stdin.readline().rstrip())))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(n, m, k, a, mask):
    s1, s2 = 0, 0
    ones = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mask[i][j] == 0:
                s1 += a[i][j]
            else:
                s2 += a[i][j]

            if i == 0:
                if j == 0:
                    ones[i][j] = mask[i][j]
                else:
                    ones[i][j] = ones[i][j-1] + mask[i][j]
            else:
                if j == 0:
                    ones[i][j] = ones[i-1][j] + mask[i][j]
                else:
                    ones[i][j] = ones[i-1][j] + ones[i][j-1] - ones[i-1][j-1] + mask[i][j]

    diff = abs(s1 - s2)

    nums = set()

    for i in range(n-k+1):
        for j in range(m-k+1):
            s = ones[i + k - 1][j + k - 1]
            if i > 0:
                s -= ones[i - 1][j + k - 1]
            if j > 0:
                s -= ones[i + k - 1][j - 1]
            if i > 0 and j > 0:
                s += ones[i - 1][j - 1]

            nums.add(abs(s + s - k * k))

    c_gcd = -1
    for num in nums:
        if c_gcd == -1:
            c_gcd = num
        else:
            c_gcd = gcd(c_gcd, num)

    if diff == 0 or (c_gcd > 0 and diff % c_gcd == 0):
        return "YES"
    else:
        return "NO"



def main():
    for _ in range(ri()):
        n, m, k = ria()
        a = [[] for _ in range(n)]
        for i in range(n):
            a[i] = ria()
        mask = [[] for _ in range(n)]
        for i in range(n):
            mask[i] = ria2()

        ws(solve(n, m, k, a, mask))


if __name__ == '__main__':
    main()
