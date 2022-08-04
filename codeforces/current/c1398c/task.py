import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    pre = [0] * (n + 1)
    cnt = {0: 1}
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
        d = pre[i+1] - i - 1
        if d not in cnt:
            cnt[d] = 0
        cnt[d] += 1

    ans = 0
    for k, v in cnt.items():
        if v > 0:
            ans += v * (v - 1) // 2

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = [int(si) for si in rs()]
        wi(solve(n, a))


if __name__ == '__main__':
    main()
