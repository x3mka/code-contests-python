import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n):
    k2 = 0
    while n % 2 == 0:
        k2 += 1
        n /= 2
    k3 = 0
    while n % 3 == 0:
        k3 += 1
        n /= 3
    if n > 1:
        return -1

    if k2 > k3:
        return -1

    return (k3 - k2) + k3

def main():
    for _ in range(ri()):
        n = ri()
        wi(solve(n))


if __name__ == '__main__':
    main()
