def rs(): return input().strip()
def ri(): return int(input())
def ria(): return list(map(int, input().split()))
def ia_to_s(a): return ' '.join([str(s) for s in a])



def solve(n):
    a = []
    tens = 1
    while n > 0:
        d = n % 10
        n //= 10
        if d > 0:
            a.append(d * tens)
        tens *= 10
    return a


def main():
    for _ in range(ri()):
        n = ri()
        a = solve(n)
        print(len(a))
        print(ia_to_s(a))


if __name__ == '__main__':
    main()
