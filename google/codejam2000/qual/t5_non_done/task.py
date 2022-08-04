import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


from itertools import permutations, combinations


def is_latin(c, n):
    return True

def out_square(c, n):
    for i in range(n):
        ws(''.join([str(j) for j in c[i]]))

def solve(t, n, k):
    a = [i+1 for i in range(n)]
    all_perms = list(permutations(a))

    d = {}

    for c in combinations(all_perms, n):
        if is_latin(c, n):
            trace = sum([c[i][i] for i in range(n)])
            if trace not in d:
                d[trace] = []
            d[trace].append(c)

    # for i in range()

    # res = None
    # r_str = 'IMPOSSIBLE' if res is None else 'POSSIBLE'
    # ws("Case #{}: {}".format(t + 1, r_str))


def main():
    for t in range(ri()):
        n, k = ria()
        solve(t, n, k)



if __name__ == '__main__':
    main()
