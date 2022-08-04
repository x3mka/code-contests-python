import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')




def solve(n, k):
    ans = 10**18
    for last_digit in range(10):
        for nines_count in range(20):
            s = 0
            for ki in range(k + 1):
                overflow = ki + last_digit >= 10
                if overflow:
                    s += 1 + (ki + last_digit) % 10
                else:
                    s += 9 * nines_count + last_digit + ki
            if s > n:
                continue
            left = n - s

            pre = []
            if left >= 8 * (k+1):
                pre.append(8)
                left -= 8 * (k+1)

            for d in range(9, 0, -1):
                while left >= d * (k+1):
                    pre.append(d)
                    left -= d * (k+1)

            if left == 0:
                pre.reverse()
                x = int(''.join([str(d) for d in pre]) + '9' * nines_count + str(last_digit))
                ans = min(ans, x)

    return -1 if ans == 10**18 else ans



def main():
    for _ in range(ri()):
        n, k = ria()
        wi(solve(n, k))


if __name__ == '__main__':
    main()
