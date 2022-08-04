import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, k, s):
    ones_i = [i for i in range(n) if s[i] == '1']

    m = len(ones_i)
    if m == 0:
        return n // (k + 1) + (1 if n % (k + 1) > 0 else 0)

    ans = 0
    for i in range(1, len(ones_i)):
        ans += max(0, ones_i[i] - ones_i[i-1] - 1 - k) // (k+1)

    if ones_i[0] != 0:
        left = max(0, ones_i[0] - k)
        ans += left // (k + 1) + (1 if left % (k + 1) > 0 else 0)
    if ones_i[-1] != n - 1:
        left = max(0, n - (ones_i[-1] + k) - 1)
        ans += left // (k + 1) + (1 if left % (k + 1) > 0 else 0)

    return ans


def main():
    for _ in range(ri()):
        n, k = ria()
        s = rs()
        wi(solve(n, k, s))


if __name__ == '__main__':
    main()
