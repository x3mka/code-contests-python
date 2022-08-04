def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def temp_at_2k_1(h, c, k):
    return k * h + (k - 1) * c, 2 * k - 1


# issues with doubles comparison, switch to frac comparison with int multiplication
# one can derive O(1) formula from comparisons: t(2k-1) <= t < t(2k+1)=((k+1)h+kc)/(2k+1)
# a = (h - t) // (2*t - h - c)
# b = a + 1
# return(2*a + 1 if 2*t*(2*a+1)*(2*b+1) >= (2*b+1)*((a+1)*h+a*c)+(2*a+1)*((b+1)*h+b*c) else 2 * b + 1)
def solve(h, c, t):
    if t <= (h+c)//2:
        return 2

    k_left = 1
    k_right = 10**19
    while k_right - k_left > 1:
        k_mid = (k_left + k_right) // 2
        t_mid_n, t_mid_d = temp_at_2k_1(h, c, k_mid)
        if t_mid_n > t * t_mid_d:
            k_left = k_mid
        else:
            k_right = k_mid

    abs_min = (abs(2*t-(h+c)), 2)
    ans = 2
    test = [x for x in [k_left+2, k_left+1, k_left, k_left-1, k_left-2] if x > 0]
    for at in test:
        t_at_n, t_at_d = temp_at_2k_1(h, c, at)
        if abs_min[1] * abs(t_at_d * t - t_at_n) <= abs_min[0] * t_at_d:
            abs_min = (abs(t_at_d * t - t_at_n), t_at_d)
            ans = 2*at-1

    return ans


def main():
    for _ in range(ri()):
        h, c, t = ria()
        print(solve(h, c, t))


if __name__ == '__main__':
    main()
