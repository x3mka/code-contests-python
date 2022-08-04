def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])


def solve(n, m, p, q):
    p_odd = sum([1 for pi in p if pi % 2 == 1])
    p_even = n - p_odd
    q_odd = sum([1 for qi in q if qi % 2 == 1])
    q_even = m - q_odd

    return p_odd * q_odd + p_even * q_even


def main():
    for _ in range(ri()):
        n = ri()
        p = ria()
        m = ri()
        q = ria()
        print(solve(n, m, p, q))


if __name__ == '__main__':
    main()
