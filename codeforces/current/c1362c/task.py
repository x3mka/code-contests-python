import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


import math


def solve_k(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return 2 * solve_k(k-1) + k


def diff_n_n1(n):
    bit_len = n.bit_length()
    s1 = bin(n)[2:].rjust(bit_len, '0')
    s2 = bin(n-1)[2:].rjust(bit_len, '0')
    return sum([1 for i in range(bit_len) if s1[i] != s2[i]])


def count(n):
    cnt = 0
    for i in range(1, n+1):
        cnt += diff_n_n1(n)
    return cnt

def solve(n):
    # diffs = [diff_n_n1(i) for i in range(1, 21)]
    # counts = [diffs[0]]
    # for i in range(1, 20):
    #     counts.append(counts[i-1] + diffs[i])
    #
    # print(counts)
    # return
    #
    # for n in range(1, 20):
    #      print(n, count(n))
    # return

    cnt = 0

    while n > 0:
        # p = int(math.log2(n))
        p = n.bit_length() - 1
        pp = 2 ** p
        cnt += solve_k(p)
        if n >= pp:
            cnt += p + 1
        n -= pp

    return cnt


def main():
    for _ in range(ri()):
        n = ri()
        print(solve(n))


if __name__ == '__main__':
    main()
