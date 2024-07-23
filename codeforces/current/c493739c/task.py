import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    # we should know previous lower, increasing stack
    # if we know j = previous lower, then all from j+1 to i-1 work for us
    stack = []

    ans = [0] * n
    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            stack.pop()

        if stack:
            ans[i] += i - stack[-1] - 1
        else:
            ans[i] += i

        stack.append(i)

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wia(solve(n, a))


if __name__ == '__main__':
    main()
