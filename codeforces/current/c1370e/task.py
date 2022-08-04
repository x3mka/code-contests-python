import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, s, t):
    if s.count('1') != t.count('1'):
        return -1

    m1 = 0
    m2 = 0
    balance = 0
    for i in range(n):
        if s[i] == '1':
            balance += 1
        if t[i] == '1':
            balance -= 1
        m1 = max(m1, balance)
        m2 = min(m2, balance)

    return m1 - m2


def main():
    n = ri()
    s = rs()
    t = rs()
    wi(solve(n, s, t))


if __name__ == '__main__':
    main()
