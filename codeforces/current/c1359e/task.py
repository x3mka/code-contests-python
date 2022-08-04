def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


MOD = 998244353


def mul(x, y):
    return (x * y) % MOD


# y = invmod(x, p) such that x*y == 1 (mod p)
# y = x**(p-2) mod p   , if p is prime
def inv(x):
    return pow(x, MOD-2, MOD)


def divide(x, y):
    return mul(x, inv(y))


def factorials_up_to_n(n):
    z = [0] * (n+1)
    z[0] = 1
    for i in range(1, n+1):
        z[i] = mul(i, z[i-1])
    return z


fact = []


def c_nk(n, k):
    global fact
    if k > n:
        return 0
    return divide(fact[n], mul(fact[n - k], fact[k]))


def solve(n, k):
    global fact
    fact = factorials_up_to_n(n)
    ans = 0
    for i in range(1, n+1):
        d = n // i
        ans = (ans + c_nk(d-1, k-1)) % MOD
    return ans


def main():
    n, k = ria()
    print(solve(n, k))


if __name__ == '__main__':
    main()
