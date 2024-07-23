import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')



def main():
    n = ri()
    a = ria()
    ans = -sys.maxsize+1
    ans_l = ans_r = 0
    max_ending_here = 0
    l = 0
    for r in range(n):
        max_ending_here += a[r]
        if max_ending_here > ans:
            ans = max_ending_here
            ans_l = l
            ans_r = r
        if max_ending_here < 0:
            max_ending_here = 0
            l = r+1
    wia([ans_l+1, ans_r+1, ans])


if __name__ == '__main__':
    main()
