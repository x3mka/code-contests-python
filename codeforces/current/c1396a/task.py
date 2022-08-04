import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(r, g, b, w):
    n = r + g + b + w
    odd_cnt = (1 if r % 2 else 0) + (1 if g % 2 else 0) + (1 if b % 2 else 0) + (1 if w % 2 else 0)

    if n % 2 == 0:
        return odd_cnt == 0
    else:
        return odd_cnt == 1


def main():
    for _ in range(ri()):
        r, g, b, w = ria()
        ans = solve(r, g, b, w)
        if not ans and r > 0 and g > 0 and b > 0:
            ans = solve(r - 1, g - 1, b - 1, w + 1)
        if ans:
            ws('YES')
        else:
            ws('NO')


if __name__ == '__main__':
    main()
