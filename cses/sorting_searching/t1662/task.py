import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def main():
    n = ri()
    a = ria()

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = (pre[i] + a[i]) % n

    ans = 0
    s = {}

    for i in range(n + 1):
        rem = pre[i]
        if rem in s:
            ans += s[rem]
        if pre[i] not in s:
            s[pre[i]] = 0
        s[pre[i]] += 1

    wi(ans)


if __name__ == '__main__':
    main()
