import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def is_sorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True


def solve(n, a, b):
    t0 = [a[i] for i in range(n) if b[i] == 0]
    t1 = [a[i] for i in range(n) if b[i] == 1]

    t0_sorted = is_sorted(t0)
    t1_sorted = is_sorted(t1)

    if t0_sorted and t1_sorted:
        return True

    return len(t0) > 0 and len(t1) > 0


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        b = ria()
        wi('Yes' if solve(n, a, b) else 'No')


if __name__ == '__main__':
    main()
