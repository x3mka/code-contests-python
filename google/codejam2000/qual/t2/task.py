import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(s):
    s = [int(si) for si in s]
    n = len(s)

    ans = []
    balance = 0
    for i in range(n):
        if s[i] > balance:
            for _ in range(s[i] - balance):
                ans.append('(')
        elif s[i] < balance:
            for _ in range(balance - s[i]):
                ans.append(')')
        balance = s[i]
        ans.append(str(s[i]))

    if balance > 0:
        for _ in range(balance):
            ans.append(')')
    return ''.join(ans)


def main():
    for t in range(ri()):
        s = rs()
        ws("Case #{}: {}".format(t+1, solve(s)))


if __name__ == '__main__':
    main()
