import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def least_prime_factor(n):
    """O(n*log(log(n))) complexity and O(n) memory"""
    """Useful when n less than 10^7, otherwise memory errors"""
    lp = [0] * (n + 1)
    lp[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            for j in range(2 * i, n + 1, i):
                if lp[j] == 0:
                    lp[j] = i
    return lp

lp = least_prime_factor(10**6)

def solve(n):
    ans = 0
    for m in range(n, 1, -1):
        ans = max(ans, n // lp[m])

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        wi(solve(n))


if __name__ == '__main__':
    main()
