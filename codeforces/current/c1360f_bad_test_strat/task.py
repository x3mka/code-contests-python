def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def dist(s1, s2):
    m = len(s1)
    return sum(1 for i in range(m) if s1[i] != s2[i])


def solve(n, m, s):
    for j in range(m):
        x = [si for si in s[0]]
        for c in range(26):
            x[j] = chr(ord('a')+c)
            ok = True
            for i in range(1, n):
                if dist(x, s[i]) > 1:
                    ok = False
                    break

            if ok:
                return ''.join(x)

    return "-1"


def main():
    for _ in range(ri()):
        n, m = ria()
        s = []
        for __ in range(n):
            s.append(rs())
        print(solve(n, m, s))


if __name__ == '__main__':
    main()
