import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


# def solve(n, a, b):
#     res = []
#     for i in range(n-1, -1, -1):
#         if a[i] == b[i]:
#             continue
#         if a[0] == b[i]:
#             a[0] = 1 - a[0]
#             res.append(1)
#
#         if i % 2 == 0:
#             a[i // 2] = 1 - a[i // 2]
#         for j in range((i + 1) // 2):
#             a[j], a[i - j] = 1 - a[i - j], 1 - a[j]
#         res.append(i + 1)
#
#     return [len(res)] + res

def solve(n, a, b):
    a.append(0)
    b.append(0)

    res1 = []
    res2 = []
    for i in range(n):
        if a[i] != a[i+1]:
            res1.append(i+1)
        if b[i] != b[i+1]:
            res2.append(i+1)

    res = res1 + res2[::-1]

    return [len(res)] + res


def main():
    for _ in range(ri()):
        n = ri()
        a = [int(si) for si in rs()]
        b = [int(si) for si in rs()]
        wia(solve(n, a, b))


if __name__ == '__main__':
    main()
