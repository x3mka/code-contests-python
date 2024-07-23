import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')



def solve(n, a):
    left_extension = [0] * n
    right_extension = [0] * n
    cover = [0] * n
    ans = a[0]
    for i in range(n):
        for j in range(i-1, -1, -1):
            if a[j] >= a[i]:
                left_extension[i] += 1
            else:
                break
        for j in range(i+1, n):
            if a[j] >= a[i]:
                right_extension[i] += 1
            else:
                break
        cover[i] = a[i] * (left_extension[i] + right_extension[i] + 1)
        ans = max(ans, cover[i])
    wia(left_extension)
    wia(right_extension)
    wia(cover)
    return ans

def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        wi(solve(n, a))


if __name__ == '__main__':
    main()
