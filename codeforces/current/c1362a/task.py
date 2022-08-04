import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')



def solve(a, b):
    if a == b:
        return 0

    if b > a:

        if b % a > 0:
            return -1
        k = b // a

    else:

        if a % b > 0:
            return -1
        k = a // b

    cnt = 0
    while k >= 8 and k % 8 == 0:
        k //= 8
        cnt += 1
    while k >= 4 and k % 4 == 0:
        k //= 4
        cnt += 1
    while k >= 2 and k % 2 == 0:
        k //= 2
        cnt += 1
    return cnt if k <= 1 else -1


def main():
    for _ in range(ri()):
        a, b = ria()
        print(solve(a, b))


if __name__ == '__main__':
    main()
