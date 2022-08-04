import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def bit_count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n & (n - 1)
    return cnt


def ok(n, mask1, mask2):
    for i in range(n-1):
        cnt = (1 if mask1 & (1 << i) else 0) + (1 if mask2 & (1 << i) else 0) + (1 if mask1 & (1 << (i+1)) else 0) + (1 if mask2 & (1 << (i+1)) else 0)
        if cnt % 2 == 0:
            return False
    return True


def solve(n, m, a):
    if n == 1:
        return 0
    if n >= 4:
        return -1

    p2 = 2**n
    inf = float('inf')

    b = [0] * m

    for j in range(m):
        mask = 0
        for i in range(n):
            if a[i][j] == 1:
                mask |= (1 << i)
        b[j] = mask

    dp = [[inf] * p2 for _ in range(m)]  # j is a mast of last col
    for mask in range(p2):
        dp[0][mask] = bit_count(b[0] ^ mask)  # number of different bits in b[0] and mask

    # precalc allowed next mask
    masks = [[] for _ in range(p2)]
    for mask1 in range(p2):
        for mask2 in range(p2):
            if ok(n, mask1, mask2):
                masks[mask1].append(mask2)

    for i in range(1, m):
        for prev_mask in range(p2):
            for next_mask in masks[prev_mask]:
                dp[i][next_mask] = min(dp[i][next_mask], dp[i-1][prev_mask] + bit_count(b[i] ^ next_mask))

    return min(dp[-1])


def main():
    n, m = ria()
    a = []
    for i in range(n):
        a.append([int(si) for si in rs()])

    wi(solve(n, m, a))


if __name__ == '__main__':
    main()
