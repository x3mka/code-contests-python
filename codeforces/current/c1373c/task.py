import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


inf = 10**18


def org(s):
    res = 0
    for init in range(10**9):
        cur = init
        ok = True
        for i in range(len(s)):
            res += 1
            if s[i] == '+':
                cur = cur + 1
            else:
                cur = cur - 1
            if cur < 0:
                ok = False
                break
        if ok:
            break

    return res


def my(s):
    n = len(s)
    d = [inf] * (n+2)
    c = 0
    for i in range(n):
        if s[i] == '+':
            c += 1
        else:
            c -= 1
        if c < 0:
            d[-c] = min(d[-c], i)

    ans = 0
    for i in range(1, n+2):
        if d[i] == inf:
            ans += n
            break
        else:
            ans += d[i] + 1

    return ans


def generate_case():
    for i in range(100):
        s = format(i, 'b').replace('1','+').replace('0','-')
        res1 = org(s)
        res2 = my(s)
        if res1 != res2:
            ws("{0}: {1} and {2}".format(s, res1, res2))
            break


def solve(s):
    return my(s)


def main():
    for _ in range(ri()):
        s = rs()
        wi(solve(s))


if __name__ == '__main__':
    main()
