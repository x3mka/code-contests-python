import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n):
    a = [i+1 for i in range(n)]

    # ok = True
    # for k in range(1, n+1):
    #     s = sum([a[i] for i in range(n) if ((i+1) % k) == 0])
    #     if s % k > 0:
    #         ok = False
    #         ws("Stop!")
    #         wia([n, k, s])
    #         wia(a)
    #         break

    return a

def main():
    for _ in range(ri()):
        n = ri()
        wia(solve(n))


if __name__ == '__main__':
    main()
