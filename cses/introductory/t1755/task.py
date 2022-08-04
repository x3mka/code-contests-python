import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter


def main():
    s = rs()
    n = len(s)
    c = Counter(s)

    odds = sum([1 for k, v in c.items() if v % 2 == 1])
    if odds >= 2 or odds == 1 and n % 2 == 0:
        ws('NO SOLUTION')
        return

    a = [''] * n
    if n % 2 == 1:
        mid = [k for k, v in c.items() if v % 2 == 1][0]
        a[n // 2] = mid
        c[mid] -= 1
    i = 0
    for k, v in c.items():
        for j in range(v//2):
            a[i] = k
            a[n-i-1] = k
            i += 1
    ws(''.join(a))


if __name__ == '__main__':
    main()
