import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')



def solve(n, a, b):
    bi = [0] * (n+1)
    for i in range(n):
        bi[b[i]] = i

    d = {}
    for i in range(n):
        s = (i - bi[a[i]] + n) % n
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

    return max(d.values())


def main():
    n = ri()
    a = ria()
    b = ria()
    wi(solve(n, a, b))


if __name__ == '__main__':
    main()
