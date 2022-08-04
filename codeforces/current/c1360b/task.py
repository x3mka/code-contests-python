def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, s):
    s = sorted(s, reverse=True)
    m = abs(s[1]-s[0])
    for i in range(1, n):
        m = min(m, abs(s[i]-s[i-1]))
    return m


def main():
    for _ in range(ri()):
        n = ri()
        s = ria()
        print(solve(n, s))


if __name__ == '__main__':
    main()
