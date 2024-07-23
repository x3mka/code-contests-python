import sys
from collections import Counter


def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, a):
    ones = a.count('1')
    zeros = len([s for s in a.split('1') if s != ''])

    # b = [a[0]]
    # for i in range(1, n):
    #     if a[i] == '1' or a[i] == '0' and a[i-1] == '1':
    #         b.append(a[i])
    return 'Yes' if ones > zeros else 'No'


    # k1, k0 = 0, 0
    # for i in range(n):
    #     if a[i] == '1':
    #         k1 += 1
    #     else:
    #         if i == 0 or a[i-1] == '1':
    #             k0 += 1
    # return "Yes" if k1 > k0 else "No"

    # ok = 0
    # if a.count("111") >= 1:
    #     ok = 1
    # if a.count("11") >= 2:
    #     ok = 1
    # if a.count("11") >= 1 and (a[0] == "1" or a[-1] == "1"):
    #     ok = 1
    # if a[0] == "1" and a[-1] == "1":
    #     ok = 1
    # return "Yes" if ok else "No"

def main():
    for _ in range(ri()):
        n = ri()
        s = rs()
        ws(solve(n, s))


if __name__ == '__main__':
    main()
