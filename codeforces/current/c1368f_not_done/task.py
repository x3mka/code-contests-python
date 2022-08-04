import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n'); sys.stdout.flush()
def wi(n): sys.stdout.write(str(n) + '\n'); sys.stdout.flush()
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n'); sys.stdout.flush()


a = []
n = 0

def ask(ax):
    for i in range(len(ax)):
        a[ax[i]] = 1
    wia([len(ax)] + [ai + 1 for ai in ax])
    ans = ri()
    if ans == -1:
        exit()
    for i in range(len(ax)):
        a[(ans + i - 1) % n] = 0


def solve():
    if n <= 3:
        wi(0)
        return

    global a
    a = [0] * n
    ask(list(range(n)))


    moves = 1

    while moves < 10000:
        off_count = sum([1 for ai in a if ai == 0])
        if off_count <= 3:
            break
        an = (off_count + 1) // 2

        nn = []
        i = 0
        while i < n and len(nn) < an:
            if a[i] == 0:
                nn.append(i)
                i += 2
            else:
                i += 1


        # best = 0
        # best_i = 0
        # s = 0
        # for r in range(n):
        #     if a[r] == 0:
        #         s += 1
        #         if s > best:
        #             best = s
        #             best_i = r - s + 1
        #     else:
        #         s = 0
        #
        # if best <= 3:
        #     break
        # nn = [i for i in range(best_i, best_i + best) if i % 2 == 0]

        ask(nn)
        moves += 1

    wi(0)


def main():
    global n
    n = ri()
    solve()


if __name__ == '__main__':
    main()
