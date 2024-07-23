import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    stack = []  # increasing, each element in stack is greater than deeper one, max is on top

    ans = [0] * n
    for i in range(n):
        while stack and stack[-1] > a[i]:
            stack.pop()

        # before insert, len of stack is number of elements less than given
        ans[i] = len(stack)
        stack.append(a[i])

    return ans


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wia(solve(n, a))


if __name__ == '__main__':
    main()
