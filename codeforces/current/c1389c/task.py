import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


from collections import Counter


def solve(s):
    n = len(s)
    best = 2

    c = Counter(s)
    for k, v in c.items():
        if v > best:
            best = v

    for sd1 in c.keys():
        for sd2 in c.keys():
            if sd1 == sd2:
                continue

            if c[sd1] + c[sd2] <= best:
                continue

            d1_idx = []
            d2_idx = []
            for i in range(n):
                if s[i] == sd1:
                    d1_idx.append(i)
                if s[i] == sd2:
                    d2_idx.append(i)
            cnt = 0
            last = sd2
            last_i = -1
            i = 0
            j = 0
            while i < len(d1_idx) or j < len(d2_idx):
                if last == sd1:
                    while j < len(d2_idx) and d2_idx[j] < last_i:
                        j += 1
                    if j < len(d2_idx):
                        last = sd2
                        last_i = d2_idx[j]
                        j += 1
                        cnt += 1
                    else:
                        break
                else:
                    while i < len(d1_idx) and d1_idx[i] < last_i:
                        i += 1
                    if i < len(d1_idx):
                        last = sd1
                        last_i = d1_idx[i]
                        i += 1
                        cnt += 1
                    else:
                        break
            if cnt % 2 == 1:
                cnt -= 1
            if cnt > best:
                best = cnt

    return n - best


def main():
    for _ in range(ri()):
        s = rs()
        wi(solve(s))


if __name__ == '__main__':
    main()
